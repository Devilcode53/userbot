import logging
import os

logger = logging.getLogger("Userbot")

def load_modules(client):
    """Dynamically load modules."""
    logger.info("Loading modules...")
    modules_dir = os.path.dirname(__file__)
    for file in os.listdir(modules_dir):
        if file.endswith(".py") and file != "__init__.py":
            module_name = file[:-3]
            try:
                # Import the module and call its setup function
                module = __import__(f"modules.{module_name}", fromlist=["setup"])
                if hasattr(module, "setup"):
                    module.setup(client)  # Pass client to the module's setup function
                logger.info(f"Loaded module: {module_name}")
            except Exception as e:
                logger.error(f"Failed to load module {module_name}: {e}")
