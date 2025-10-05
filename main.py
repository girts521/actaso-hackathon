import os
import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram_handles import start, handle_message
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURATION ---
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN") 
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 
GOOGLE_SHEETS_CREDENTIALS_FILE = os.getenv("GOOGLE_SHEETS_CREDENTIALS_FILE") 
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID") 
SHEET_NAME = os.getenv("SHEET_NAME") 

# --- CATEGORIES & ACCOUNTS ---
CATEGORIES = [
    "Groceries", "Transport", "Dining Out", "Shopping", "Housing",
    "Utilities", "Health & Wellness", "Entertainment", "Subscriptions",
    "Personal Care", "Miscellaneous"
]
ACCOUNTS = ["Girts", "Thao", "Default"]
STATUS_OPTIONS = ["✅", "🅿️", "*<fe0f><20e3>"]

# --- LOGGING SETUP ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    # Command handlers
    application.add_handler(CommandHandler("start", start))
    # Message handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == '__main__':
    main()
