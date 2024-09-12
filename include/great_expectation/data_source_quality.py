import sys
import pandas as pd
from datetime import datetime
import subprocess
from airflow.models import Variable

sys.path.append("/usr/local/airflow/include/great_expectation")
from mail_alert import *
password = Variable.get("my_outlook_password")

alert_quality = mail_alert()

# def install_package(package_name):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# # Install the package
# install_package("great-expectations")

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
    message = f"""Task 1: Check file exist -> Success 
File: {file_path} exists"""
    
else:
    message = f"""Task 1: Check file exist -> Failed 
File: {file_path} does not exists"""

subject = "Data Quality Check for Source"

alert_quality.send_email(
    body= f"""Subject: {subject}

{message}. 

Please review the attached report and fix the error.""",

    to_email="20520270@gm.uit.edu.vn",

    password=password
)
