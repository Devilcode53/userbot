from telethon.tl.functions.users import GetFullUserRequest
from main import client, OWNER_ID
import logging
from telethon.errors import UserIdInvalidError
from telethon import TelegramClient, events

# Logging setup
logger = logging.getLogger("Userbot")
logger.info("Info module loaded successfully.")

def setup(client):
    @client.on(events.NewMessage(pattern=r'\.info', from_users=OWNER_ID))
    async def info_handler(event):
        try:
            # Ensure the command is used in reply to a message
            replied_message = await event.get_reply_message()
            if not replied_message:
                await event.reply("❌ **Please reply to a user to use `.info`.**")
                return

            # Get the sender of the replied message
            user = await replied_message.get_sender()

            # Extract user details
            name = user.first_name or "No Name"
            last_name = user.last_name or ""
            full_name = f"{name} {last_name}".strip()
            username = f"@{user.username}" if user.username else "No Username"
            user_id = user.id
            is_bot = "False" if not user.bot else "True"
            is_verified = "True" if user.verified else "False"
            is_restricted = "True" if getattr(user, "restricted", False) else "False"

            # Fetch profile photos and Data Centre ID
            profile_photos = await client.get_profile_photos(user.id)
            profile_pic_count = len(profile_photos)
            dc_id = user.photo.dc_id if user.photo else "Unknown"

            # Use GetFullUserRequest to fetch more details, including bio
            full_user = await client(GetFullUserRequest(user.id))
            bio = full_user.about if hasattr(full_user, 'about') else "No bio available"

            # Permanent link to the user's profile
            permanent_link = f"[{full_name}](tg://user?id={user_id})"

            # Construct the message to send
            result = (
                f"**USER INFO from Devil's Database:**\n\n"
                f"👤 **Name:** {full_name}\n"
                f"👦 **Username:** {username}\n"
                f"✉ **ID:** `{user_id}`\n"
                f"🌎 **Data Centre ID:** {dc_id}\n"
                f"🖼️ **Number of Profile Pics:** {profile_pic_count}\n"
                f"🤖 **Is Bot:** {is_bot}\n"
                f"🕛 **Is Restricted:** {is_restricted}\n"
                f"✅ **Is Verified by Telegram:** {is_verified}\n\n"
                f"✍ **Bio:** {bio}\n\n"
                f"🔗 **Permanent Link to Profile:** {permanent_link}"
            )

            # Send profile picture with the information if available
            if profile_photos:
                await event.reply(result, file=profile_photos[0])
            else:
                await event.reply(result)

        except UserIdInvalidError:
            # Handle invalid user ID errors
            await event.reply("❌ **Failed to retrieve user info. The user ID is invalid.**")
        except Exception as e:
            # Handle any other errors
            await event.reply(f"❌ **Failed to retrieve user info.**\nError: {e}")
