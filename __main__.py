from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from logger import configure_logger
from services.db_manager import db_client
from engine.tools import Tools
from engine.engine import Engine
from services.appointment_manager import AppointmentManager
import handlers
import config

# Initialize logger
logger = configure_logger()

if not config.TELEGRAM_BOT_TOKEN or not config.HEROKU_APP_NAME:
    raise ValueError("TELEGRAM_BOT_TOKEN and HEROKU_APP_NAME environment variables must be set")


def main():
    # Create the Application and pass it your bot's token.
    application = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    # Initialize your components with the necessary configuration
    tools = Tools(config.OPENAI_API_KEY)  # Initialize Tools with the OpenAI API key
    appointment_manager = AppointmentManager()
    application.bot_data["engine"] = Engine(tools.builder, appointment_manager)

    # Register handlers with the Application
    application.add_handlers([
        CommandHandler("start", handlers.start),
        CommandHandler("help", handlers.help_),
        CommandHandler("cancel", handlers.cancel),
        MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.message_handler),
    ])

    # Start the bot with webhook
    if config.DEPLOY_MODE == "webhook":
        application.run_webhook(
            listen="0.0.0.0",
            port=config.PORT,
            url_path=config.TELEGRAM_BOT_TOKEN,
            webhook_url=f"https://{config.HEROKU_APP_NAME}.herokuapp.com/{config.TELEGRAM_BOT_TOKEN}"
        )
    elif config.DEPLOY_MODE == "polling":
        application.run_polling()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.warning("Exception occurred", exc_info=True)
    finally:
        db_client.close_db()
        logger.info("Bot stopped.")
