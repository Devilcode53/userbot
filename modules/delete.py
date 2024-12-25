from telethon import TelegramClient, events
from telethon.tl.functions.messages import DeleteMessagesRequest
from telethon.tl.types import PeerChat, PeerUser
import asyncio

from main import client

# Logging setup
import logging
logger = logging.getLogger("Userbot")
logger.info("Delete module loaded successfully.")

# Mass delete delay
DELETE_DELAY = 0.1  # Delay between each message delete to avoid flooding Telegram API

async def delete_all_messages(chat_id, user_id=None):
    """Delete all messages from the given user (or bot) in the chat."""
    try:
        # Fetch all messages from the chat
        async for message in client.iter_messages(chat_id):
            if user_id and message.sender_id == user_id:  # Delete messages only from the specified user
                await client(DeleteMessagesRequest([message.id]))
                await asyncio.sleep(DELETE_DELAY)
            elif not user_id and message.sender_id == client.user_id:  # Delete bot's messages
                await client(DeleteMessagesRequest([message.id]))
                await asyncio.sleep(DELETE_DELAY)
        logger.info(f"Successfully deleted all messages from user {user_id} in chat {chat_id}.")
    except Exception as e:
        logger.error(f"Error deleting messages: {e}")

def setup(client):
    # .adel command to delete all of a specific user's messages or bot's messages
    @client.on(events.NewMessage(pattern=r'\.adel'))
    async def adel_handler(event):
        try:
            if event.is_private:  # If it's a private chat, handle accordingly
                await event.reply("❌ **This command only works in groups.**")
                return

            replied_message = await event.get_reply_message()

            # Get the target user from the reply (or the sender of the command if no reply)
            target_user = replied_message.sender_id if replied_message else event.sender_id

            await event.reply("⏳ **Deleting messages... This may take some time.**")
            
            # Call the mass delete function
            await delete_all_messages(event.chat_id, target_user)
            
            await event.reply("✅ **All messages have been deleted.**")
        
        except Exception as e:
            await event.reply(f"❌ **Failed to delete messages.**\nError: {e}")

    # .del command to delete the replied-to message
    @client.on(events.NewMessage(pattern=r'\.del'))
    async def del_handler(event):
        try:
            # Ensure the command is used in reply to a message
            replied_message = await event.get_reply_message()
            if not replied_message:
                await event.reply("❌ **Please reply to a message to delete it.**")
                return

            await event.reply("⏳ **Deleting the message...**")

            # Delete the replied message as quickly as possible
            await client(DeleteMessagesRequest([replied_message.id]))

            await event.reply("✅ **Message deleted successfully.**")

        except Exception as e:
            await event.reply(f"❌ **Failed to delete the message.**\nError: {e}")
