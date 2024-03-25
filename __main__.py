import os
import threading
from flask import Flask, request, jsonify
from logger import configure_logger
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
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

# Initialize logger
logger = configure_logger()

# Check for necessary config vars
if not config.TELEGRAM_BOT_TOKEN or not config.OPENAI_API_KEY:
    raise ValueError(
        "TELEGRAM_BOT_TOKEN and OPENAI_API_KEY env variables weren't implemented in .env (both should be initialized).")

# Initialize Flask app
app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"status": "ok"})


def run_flask_app():
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)


def run_telegram_bot():
    application = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    tools = Tools(config.OPENAI_API_KEY)  # Initialize Tools with the OpenAI API key
    appointment_manager = AppointmentManager()
    application.bot_data["engine"] = Engine(tools.builder, appointment_manager)

    application.add_handlers(
        [
            CommandHandler("start", COMMAND_HANDLERS["start"]),
            CommandHandler("help", COMMAND_HANDLERS["help"]),
            CommandHandler("cancel", COMMAND_HANDLERS["cancel"]),
            MessageHandler(filters.TEXT & ~filters.COMMAND, MESSAGE_HANDLERS["message"]),
        ]
    )

    application.run_polling()


if __name__ == "__main__":
    try:
        # Run Flask app in a separate thread
        threading.Thread(target=run_flask_app).start()
        # Run the main function for the Telegram bot
        run_telegram_bot()
    except Exception as e:
        logger.warning(traceback.format_exc())
    finally:
        db_client.close_db()
        logger.info("Bot stopped.")
