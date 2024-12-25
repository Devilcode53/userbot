from telethon import events
from main import client, OWNER_ID, start_date
import logging


#logging info

logger = logging.getLogger("Userbot")
logger.info("Start module loaded successfully.")


def setup(client):
    @client.on(events.NewMessage(pattern=r'\.help'))
    async def start_handler(event):
        await event.reply("Adding soon `.help`")