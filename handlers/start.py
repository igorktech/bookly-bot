# Helper to show start message
from logger import configure_logger
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

logger = configure_logger()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send a message when the command /start is issued."""
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    await update.message.reply_text(
        f"Hi {user.first_name}! I'm a bot that helps you manage your appointments. "
        "Send /start to start a conversation with me. "
        "Send /cancel to end the conversation."
    )

    return ConversationHandler.END
