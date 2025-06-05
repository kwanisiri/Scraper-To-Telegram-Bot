from app.models import Lead
from app.config import settings  # Import settings to access config variables
from telegram.ext import Application  # Import Application for async interface

# This function sends a message to a Telegram chat using the bot token and chat ID from your settings.
# It uses the python-telegram-bot v20+ async Application interface.
# Make sure your .env file contains TELEGRAM_TOKEN and CHAT_ID variables, and your config.py loads them.
async def notify_telegram(lead: Lead):
    BOT_TOKEN = settings.telegram_token  # Get bot token from settings
    CHAT_ID = settings.chat_id           # Get chat ID from settings
    # Build the Application (the async context for the bot)
    application = Application.builder().token(BOT_TOKEN).build()
    # Send a message asynchronously using the bot instance from the application
    await application.bot.send_message(chat_id=CHAT_ID, text=f"New Lead: {lead.name} ({lead.url}) — Score: {lead.score}")

# Learning notes:
# - This function is async, so you must use 'await notify_telegram(lead)' in your code.
# - The settings object loads values from your .env file automatically if you use Pydantic's BaseSettings.
# - python-telegram-bot v20+ uses Application for async operations. Older versions use a different (sync) API.
# - If you see errors, check your python-telegram-bot version and consult the official docs for async usage.
