import time
from telethon import events
from main import client, OWNER_ID, start_date
import logging
from datetime import datetime
import random

# Logging setup
logger = logging.getLogger("Userbot")
logger.info("Start module loaded successfully.")

# Store the start time
start_time = time.time()

def setup(client):


    # Start command handler


    @client.on(events.NewMessage(pattern=r'\.start', from_users=OWNER_ID))
    async def start_handler(event):
        # Calculate uptime
        uptime_seconds = int(time.time() - start_time)
        hours, remainder = divmod(uptime_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        uptime = f"{hours}h {minutes}m {seconds}s"

        # Custom message
        message = (
            "🌟 **Greetings, Master `Devil`🦇🕷️!**\n\n"
            "I am here, at your service, ready to obey your every command.\n\n"
            f"🕒 **Uptime:** `{uptime}`\n\n"
            "💬 Type `.help` to unleash my full potential.\n\n"
            "⚡️ **Let's make some magic happen!** ⚡️"
        )

        logger.info(".start command received.")
        await event.reply(message, link_preview=False)
        await event.delete()




    # Status command handler

    @client.on(events.NewMessage(pattern=r'\.status', from_users=OWNER_ID))
    async def status_handler(event):
        # Get uptime
        uptime_seconds = int(time.time() - start_time)
        hours, remainder = divmod(uptime_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        uptime = f"{hours}h {minutes}m {seconds}s"
    
        # Get the total number of chats the bot is part of
        dialogs = await client.get_dialogs()
        total_chats = len(dialogs)
    
        # Get the owner's details
        owner = await client.get_entity(OWNER_ID)
        owner_username = f"[Devil](tg://user?id={OWNER_ID})"  
    
        days_active = (datetime.now() - start_date).days
        start_date_str = start_date.strftime("%B %d, %Y")  # Example: "December 23, 2024"


        message = (
            f"🤖 **Userbot Status Report** 🤖\n\n"
            f"💠 **Owner:** {owner_username} (`{OWNER_ID}`)\n"
            f"🕒 **Uptime:** `{uptime}`\n"
            f"📅 **Started On:** {start_date_str} ({days_active} days active)\n"
            f"💬 **Connected Chats:** `{total_chats}`\n"
            f"⚙️ **Bot Version:** `1.0`\n\n"
            "🚀 **Bot is running smoothly!**\n"
        )
    
        # Send the status report
        await event.reply(message, link_preview=False)
        await event.delete()
    

    #hack command block

    @client.on(events.NewMessage(pattern=r'\.hack', from_users=OWNER_ID))
    async def hack_handler(event):
        # Initialize the hack sequence
        hack_sequence = [
            "💻 **Initializing Hack Mode...**",
            "⚡️ **Bypassing security protocols...**",
            "🔓 **Accessing target system...**",
            "⏳ **Decrypting data...**"
        ]

        # Send the initial messages with delays
        for step in hack_sequence:
            await event.edit(step)
            time.sleep(1)  # Wait 1 second between messages

        # Now show the cool progress bar from 0% to 100%
        await event.edit("💻 **Hack in progress...**")
        for progress in range(0, 101, 20):  # Progress from 0% to 100%
            # Create a fancy progress bar using emojis
            completed = "◻️" * (progress // 10)  # Filled portion
            remaining = "◼️" * (10 - progress // 10)  # Empty portion
            progress_bar = f"[{completed}{remaining}] {progress}%"
            await event.edit(progress_bar)
            time.sleep(0.5)  # Update every second


        owner_username = f"[Devil](tg://user?id={OWNER_ID})" 

        
        completion_message = (
            f"💻 **Welcome, {owner_username}!**\n"
            "🔓 **Access granted to the system.**\n\n"
            "⚡️ **System detected: Vulnerable.**\n"
            "🔐 **Releasing full control of the system...**\n"
            "🕷️ **Prepare for chaos.**"
        )
        await event.edit(completion_message)
    
