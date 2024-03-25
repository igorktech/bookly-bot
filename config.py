import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DEPLOY_MODE = os.getenv("DEPLOY_MODE", "polling")
PORT = os.getenv("PORT", 8000)
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
