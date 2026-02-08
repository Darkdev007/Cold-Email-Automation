import smtplib
import os
import json
from email.message import EmailMessage
from  src.llm import generated_subject
from src.utils import get_project_logger, return_data_path
from dotenv import load_dotenv


load_dotenv()
EMAIL_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL_ADDRESS = os.getenv("SMTP_EMAIL")
logger = get_project_logger("email_messages")
#Email credentials
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_EMAIL = EMAIL_ADDRESS
SMTP_PASSWORD = EMAIL_PASSWORD
EMAILS_PATH = return_data_path()

def load_emails():
    with open(EMAILS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
    
def send_emails():
    emails = load_emails()
    for email in emails:
        to_email = email["to"][0] if isinstance(email["to"], list) else email["to"]
        msg = EmailMessage()
        msg["From"] = SMTP_EMAIL
        msg["To"] = to_email
        msg["Subject"] = generated_subject
        msg.set_content(email["body"])

        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.send_message(msg)
            server.quit()
            logger.info(f"Sent to {email['company']}")
        except Exception as e:
            logger.info(f"Failed to send to {email['company']}: {str(e)}")

