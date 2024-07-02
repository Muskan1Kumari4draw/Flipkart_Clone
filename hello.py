import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Email credentials
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"  # Use App Password if 2FA is enabled

# Email content
def create_email():
    subject = "Daily Report"
    body = "This is the body of your daily report."
    
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS  # Can be a list of recipients
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    return msg

# Send email
def send_email():
    try:
        msg = create_email()

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")

# Schedule email to be sent daily
schedule.every().day.at("09:00").do(send_email)  # Set the desired time

print("Email scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(60)
