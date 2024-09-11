import requests
import time
import sys
import pandas as pd
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Install package
import subprocess
import sys

# def install_package(package_name):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# # Install the package
# install_package("great_expectations")

import great_expectations as gx


# Greate Expectation Configuration
context = gx.get_context()

import os

def check_local_file(file_path):
    """Check if a file exists in the local filesystem."""
    return os.path.isfile(file_path)

# Specify the file path
file_path = '/usr/local/airflow/include/dataset/Online_Retail.csv'

# Run the check
if check_local_file(file_path):
    message = f"File {file_path} exists."
else:
    message = f"File {file_path} does not exist."


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Your email credentials
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USER = 'nguyenthanhphat2669@gmail.com'
GMAIL_PASSWORD = 'Thanhphat2609@'  # Consider using an App Password if 2FA is enabled

# Email content
def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Create server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Secure the connection

    try:
        # Login Credentials for sending the email
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        # Send email
        server.sendmail(GMAIL_USER, to_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    finally:
        server.quit()

# Example usage
send_email(
    subject="Data Quality Check",
    body="This is a Quality Test Data email sent from Python. Please review the attached report.",
    to_email="20520270@gm.uit.edu.vn"
)
