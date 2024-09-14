import sys
import pandas as pd
from datetime import datetime
import subprocess
from hdfs import InsecureClient
from airflow.models import Variable

from mail_alert import *
password = Variable.get("my_outlook_password")

alert_quality = mail_alert()

import great_expectations as gx

# Greate Expectation Configuration
context = gx.get_context()

import os

# To connect to WebHDFS by providing the IP of the HDFS host and the WebHDFS port.
client_hdfs = InsecureClient('http://hdfs-namenode:9870', user='thanhphat')

def file_exists(client_hdfs, path):
    try:
        client_hdfs.status(path)
        return True
    except Exception as e:
        return False

file_path = '/Online_Retail_Analysis/datalake/online_retail.csv'

# Task 1: Check exits File
if file_exists(client_hdfs, file_path):
    message_task_1 = f"""Task 1: Check file exists. File: {file_path} exists => Success"""
else:
    message_task_1 = f"""Task 1: Check file exists. File: {file_path} does not exists => Failed"""

with client_hdfs.read('/Online_Retail_Analysis/datalake/online_retail.csv', encoding = 'utf-8') as reader:
    df = pd.read_csv(reader)
    df.to_csv("./online_retail.csv", index=False, header=True)


validator = context.sources.pandas_default.read_csv("./online_retail.csv")

# Task 2: Check schema of the data source
col_check = ["InvoiceNo", "StockCode", "Description", "Quantity", 
                 "InvoiceDate", "UnitPrice", "CustomerID", "Country"]

validator.expect_table_columns_to_match_set(col_check, exact_match=True)


# Task 3: Check null value
validator.expect_column_values_to_not_be_null(column="InvoiceNo")
validator.expect_column_values_to_not_be_null(column="CustomerID")
validator.expect_column_values_to_not_be_null(column="StockCode")


# Run the validator

validation_results = validator.validate()

# print(validation_results)

# Task message
task_messages = []

for index, result in enumerate(validation_results['results']):
    expectation_type = result['expectation_config']['expectation_type']
    
    # Default value for column to avoid errors
    column = result['expectation_config']['kwargs'].get('column', 'N/A')
    
    task_check = index + 2 

    # Check for success or failure in the result
    if result['success']:
        if expectation_type == "expect_table_columns_to_match_set":
            message = f"Task {task_check}: Check schema. All columns match => Success"
        else:
            message = f"Task {task_check}: Check null value for column: {column} => Success"
    else:
        if expectation_type == "expect_table_columns_to_match_set":
            message = f"Task {task_check}: Check schema. Columns do not match => Failed"
        else:
            message = f"Task {task_check}: Check null value for column: {column} => Failed"
        
    task_messages.append(message)

# Combine file check message with task messages
final_message = f"{message_task_1}\n" + "\n".join(task_messages)

print(final_message)

subject = "Data Quality Check for Source"

alert_quality.send_email(
    body= f"""Subject: {subject}

{final_message}. 

Please review the attached report and fix the error.""",

    to_email="20520270@gm.uit.edu.vn",

    password=password
)

os.remove("./online_retail.csv")
