import google.generativeai as genai
from datetime import datetime
import json
import os
import logging

logger = logging.getLogger(__name__)

# The model is declared but not initialized
ai_model = None

CATEGORIES = [
    "Groceries", "Transport", "Dining Out", "Shopping", "Housing",
    "Utilities", "Health & Wellness", "Entertainment", "Subscriptions",
    "Personal Care", "Miscellaneous"
]
ACCOUNTS = ["Girts", "Thao"]
STATUS_OPTIONS = ["✅", "🅿️", "*<fe0f><20e3>"]

# --- GEMINI AI SETUP ---
def initialize_ai():
    """Configures the AI model. Call this from main.py AFTER load_dotenv()."""
    global ai_model
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("FATAL: GEMINI_API_KEY is not set.")
    
    genai.configure(api_key=api_key)
    ai_model = genai.GenerativeModel('gemini-2.5-flash')
    logger.info("Gemini AI model initialized.")

def get_ai_transaction_details(text):
    """Uses Gemini to parse a natural language message into a transaction."""
    prompt = f"""
    You are a budget assistant. Your task is to extract transaction details from the following user message.
    The user's message is: "{text}"

    You must identify the following fields:
    1.  "amount": The numerical value of the transaction.
    2.  "category": The most appropriate category from this list: {CATEGORIES}.
    3.  "account": The person who made the transaction. Choose from this list: {ACCOUNTS}. If you cannot determine the account, set it to null.
    4.  "memo": A brief description of the transaction. This should be the original user message.

    The transaction is an expense, so the amount should be positive.
    Today's date is {datetime.now().strftime('%Y-%m-%d')}.

    Respond ONLY with a valid JSON object. Do not include any other text or explanations.
    Example response:
    {{
      "amount": 25.50,
      "category": "Groceries",
      "account": "Thao",
      "memo": "Weekly groceries"
    }}
    """
    try:
        response = ai_model.generate_content(prompt)
        cleaned_response = response.text.strip().replace("```json", "").replace("```", "").strip()
        return json.loads(cleaned_response)
    except Exception as e:
        logger.error(f"Error parsing AI response: {e}")
        logger.error(f"Raw AI response: {response.text}")
        return None

