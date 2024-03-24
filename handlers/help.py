# Helper to print help message
from logger import configure_logger
from telegram import Update
from telegram.ext import ContextTypes

logger = configure_logger()


async def help_(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    user = update.message.from_user
    logger.info("User %s asked for help.", user.first_name)
    await update.message.reply_text(
        f"Hi {user.first_name}! I'm a bot that helps you manage your appointments. "
        "Send /start to start a conversation with me. "
        "Send /cancel to end the conversation."
    )
    return
