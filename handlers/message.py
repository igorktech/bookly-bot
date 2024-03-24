# Helper to handle text interaction
from logger import configure_logger
from telegram import Update
from telegram.ext import ContextTypes
from services.appointment_manager import AppointmentManager

logger = configure_logger()


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Handle text interaction with user"""
    user = update.message.from_user
    logger.info("User %s sent a message.", user.first_name)

    user_id = user.id
    chat_id = update.message.chat_id

    appointment_manager = AppointmentManager()
    engine = context.bot_data['engine']
    engine.appointment_manager = appointment_manager

    response = engine.run_dm(chat_id, user_id, update.message.text)
    logger.info(f"Response: {response}")
    await update.message.reply_text(response)
    return
