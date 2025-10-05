from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a welcome message when the /start command is issued."""
    await update.message.reply_text(
        "Hi! I'm your personal finance tracker bot. Send me a message about a transaction "
        "(e.g., '55 for weekly groceries') and I'll add it to your Google Sheet. As simple as chatting with a friend!"
    )

