from logger import configure_logger
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)
from services.db_manager import db_client
from engine.tools import Tools
from engine.engine import Engine
from services.appointment_manager import AppointmentManager
import handlers
import config

COMMAND_HANDLERS = {
    "start": handlers.start,
    "help": handlers.help_,
    "cancel": handlers.cancel,
}

MESSAGE_HANDLERS = {
    "message": handlers.message_handler,
}

logger = configure_logger()

if not config.TELEGRAM_BOT_TOKEN or not config.OPENAI_API_KEY:
    raise ValueError(
        "TELEGRAM_BOT_TOKEN and OPENAI_API_KET env variables"
        "wasn't implemented in .env (both should be initialized)."
    )


def main():
    app = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    tools = Tools(config.OPENAI_API_KEY)  # Initialize Tools with the OpenAI API key
    appointment_manager = AppointmentManager()
    app.bot_data["engine"] = Engine(tools.builder, appointment_manager)

    app.add_handlers(
        [
            CommandHandler("start", COMMAND_HANDLERS["start"]),
            CommandHandler("help", COMMAND_HANDLERS["help"]),
            CommandHandler("cancel", COMMAND_HANDLERS["cancel"]),
            MessageHandler(filters.TEXT & ~filters.COMMAND, MESSAGE_HANDLERS["message"]),
        ]
    )

    app.run_polling()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
    finally:
        db_client.close_db()
        logger.info("Bot stopped.")
