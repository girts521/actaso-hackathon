from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from google_gemini import get_ai_transaction_details
from google_sheets import get_sheets_service
from datetime import datetime

def parse_transaction_data(transaction_data, user_message):
    try:
        service = get_sheets_service()
        new_row = [
            datetime.now().strftime('%Y-%m-%d'),
            transaction_data.get('amount', ''),
            '',
            transaction_data.get('category', 'Miscellaneous'),
            transaction_data.get('account', ''),
            transaction_data.get('memo', user_message),
            '🅿️'
        ]
    except Exception as e:
        #TODO: add logger here
        return 


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a welcome message when the /start command is issued."""
    await update.message.reply_text(
        "Hi! I'm your personal finance tracker bot. Send me a message about a transaction "
        "(e.g., '55 for weekly groceries') and I'll add it to your Google Sheet. As simple as chatting with a friend!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles regular text messages and processes them as transactions."""
    user_message = update.message.text
    await update.message.reply_text("Got it. Preparing your transaction...")

    transaction_data = get_ai_transaction_details(user_message)
    if not transaction_data:
        await update.message.reply_text("Sorry, I could not understand that... Please try again.")
        return
    
    #TODO: Parse that data and add it into google sheets
    new_row = parse_transaction_data(transaction_data, user_message)

    #TODO: Append parsed data to sheets
