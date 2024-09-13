import sys
import pandas as pd
from datetime import datetime
import subprocess
from airflow.models import Variable

from mail_alert import *
password = Variable.get("my_outlook_password")

alert_quality = mail_alert()

import great_expectations as gx

# Greate Expectation Configuration
context = gx.get_context()

import os

def check_local_file(file_path):
    """Check if a file exists in the local filesystem."""
    return os.path.isfile(file_path)

# Specify the file path
file_path = '/usr/local/airflow/include/dataset/Online_Retail.csv'

# Task 1: Check exits File
if check_local_file(file_path):
    message = f"""Task 1: Check file exist -> Success 
File: {file_path} exists"""
    
else:
    message = f"""Task 1: Check file exist -> Failed 
File: {file_path} does not exists"""


# Task 2: Check schema of the data source
try:
    validator = context.sources.pandas_default.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    try:
        df = context.sources.pandas_default.read_csv(file_path, encoding='ISO-8859-1')
    except UnicodeDecodeError:
        df = context.sources.pandas_default.read_csv(file_path, encoding='cp1252')
# Expect the columns to be from the expected column_set
expected_column_set = ["InvoiceNo", "StockCode", "Description", "Quantity", "InvoiceDate", "UnitPrice", "CustomerID", "Country"]
validator.expect_table_columns_to_match_set(expected_column_set, exact_match=True)


# Task 3: Check null value
validator.expect_column_values_to_not_be_null(column="InvoiceNo")
validator.expect_column_values_to_not_be_null(column="CustomerID")
validator.expect_column_values_to_not_be_null(column="StockCode")



# Run the validator
validation_results = validator.validate()

subject = "Data Quality Check for Source"

alert_quality.send_email(
    body= f"""Subject: {subject}

{message}. 

Please review the attached report and fix the error.""",

    to_email="20520270@gm.uit.edu.vn",

    password=password
)
