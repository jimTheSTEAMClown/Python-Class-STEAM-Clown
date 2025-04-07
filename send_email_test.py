"""
######################################################################
Simple Text Email Python Script
Coded By Robert Johns - Hackr.io
https://hackr.io/blog/how-to-send-emails-with-python-using-gmail
https://www.youtube.com/watch?app=desktop&v=QJobMzcmoMo&t=0s
Thanks For Watching!!!
######################################################################
"""
import ssl
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

# Load environment variables
# # there is a .env file in the same directory with
# "EMAIL_ADDRESS and "EMAIL_PASSWORD"
load_dotenv()

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
#print(EMAIL_ADDRESS, EMAIL_PASSWORD)

def send_email(recipient_email, subject, body, filename):
    """
    Sends an email using Gmail SMTP.
    
    Args:
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The email body content.
    """
    try:
        # Create the email meassage
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))
        
        # File to be attached
        # The filename is passed in, but you can hard
        # code it here too:
        #filename = 'path_to_your_file.txt' 
        
        # Open the file in the binary mode
        with open(filename, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            
        encoders.encode_base64(part)
        
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={filename}",
        )
        msg.attach(part)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    recipient_email = "jim.the.steam.clown@gmail.com"
    subject = "test"
    body = "hey this email worked"
    filename = "sendMail.py"
    send_email(recipient_email, subject, body,filename)

main()
