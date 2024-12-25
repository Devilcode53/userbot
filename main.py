import logging
from telethon import TelegramClient
import os
from dotenv import load_dotenv
import time
from datetime import datetime

# Logging setup
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("Userbot")

# Load environment variables from .env
load_dotenv()

# Bot configuration
API_ID = os.getenv("API_ID", "your_api_id")
API_HASH = os.getenv("API_HASH", "your_api_hash")
SESSION = os.getenv("SESSION", "your_session_name")
OWNER_ID = int(os.getenv("OWNER_ID", "your_user_id"))

client = TelegramClient(SESSION, API_ID, API_HASH)

start_date = datetime.now()

# Module loader to automatically import all modules
def load_modules(client):
    logger.info("Loading modules...")
    modules_dir = "modules"
    if not os.path.exists(modules_dir):
        os.mkdir(modules_dir)

    for file in os.listdir(modules_dir):
        if file.endswith(".py") and file != "__init__.py":
            module_name = file[:-3]  # Remove '.py' extension
            try:
                module = __import__(f"modules.{module_name}", fromlist=["setup"])
                if hasattr(module, "setup"):
                    module.setup(client)  # Pass the client instance to the module's setup function
                    logger.info(f"Loaded module: {module_name}")
                else:
                    logger.warning(f"Module {module_name} does not have a setup function.")
            except Exception as e:
                logger.error(f"Failed to load module {module_name}: {e}")


# Start the bot
if __name__ == "__main__":
    load_modules(client)  # Load all modules and pass the client
    logger.info("Starting userbot...")
    client.start()  # Start the client and connect to Telegram
    print("Userbot activated! Ready to fire.")
    client.run_until_disconnected()  # Keep the bot running until disconnected
