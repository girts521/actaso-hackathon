from google.oauth2 import service_account
from googleapiclient.discovery import build
import os


# --- GOOGLE SHEETS API SETUP ---
def get_sheets_service():
    """Authenticates and returns a Google Sheets service object."""
    GOOGLE_SHEETS_CREDENTIALS_FILE = os.getenv("GOOGLE_SHEETS_CREDENTIALS_FILE") 
    creds = service_account.Credentials.from_service_account_file(
        GOOGLE_SHEETS_CREDENTIALS_FILE,
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    service = build('sheets', 'v4', credentials=creds)
    return service
