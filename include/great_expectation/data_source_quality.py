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

def check_local_file(file_path):
    """Check if a file exists in the local filesystem."""
    return os.path.isfile(file_path)

# Specify the file path
    # file path for local check
# file_path = "../dataset/Online_Retail.csv"
    # file path for Docker
file_path = '/usr/local/airflow/include/dataset/Online_Retail.csv'

# Task 1: Check exits File
if check_local_file(file_path):
    message_task_1 = f"""Task 1: Check file exists -> Success. File: {file_path} exists"""
    
else:
    message_task_1 = f"""Task 1: Check file exists -> Failed. File: {file_path} does not exists"""

# To connect to WebHDFS by providing the IP of the HDFS host and the WebHDFS port.
client_hdfs = InsecureClient('http://hdfs-namenode:9870', user='thanhphat')

with client_hdfs.read('/Online_Retail_Analysis/datalake/online_retail.csv', encoding = 'ISO-8859-1') as reader:
    df = pd.read_csv(reader,index_col=0)

# Prepare for great_expectations quality
data_source = context.data_sources.add_pandas("pandas")
data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})


# Task 2: Check schema of the data source

expected_schema = gx.expectations.ExpectTableColumnsToMatchSet(
    column_set= ["InvoiceNo", "StockCode", "Description", "Quantity", 
                 "InvoiceDate", "UnitPrice", "CustomerID", "Country"],
    exact_match=True)


# Task 3: Check null value
expected_invoice_notnull = gx.expectations.ExpectColumnValuesToNotBeNull(
                                                column="InvoiceNo")

expected_cusid_notnull = gx.expectations.ExpectColumnValuesToNotBeNull(
                                                column="CustomerID")

expected_stockcode_notnull = gx.expectations.ExpectColumnValuesToNotBeNull(
                                                column="StockCode")


# Run the validator

validation_check = [expected_schema, expected_invoice_notnull, expected_cusid_notnull, expected_stockcode_notnull]
validation_results = []

for task_check in validation_check:
    validation = batch.validate(task_check)
    validation_results.append(validation)

# Creating task messages
task_messages = []

for idx, result in enumerate(validation_results, start=2):
    type_check = result["expectation_config"]["type"]
    column = result["expectation_config"]["kwargs"].get("column", "N/A")
    success = result["success"]
    
    if success:
        if type_check == "expect_table_columns_to_match_set":
            message = f"Task {idx}: Check schema. All column match -> Success"
        else:
            message = f"Task {idx}: Check null for column: {column} -> Success"
    else:
        if type_check == "expect_table_columns_to_match_set":
            message = f"Task {idx}: Check schema. All column not match -> Failed"
        else:
            message = f"Task {idx}: Check null for column for column: {column} -> Failed"
    
    task_messages.append(message)

# Combine file check message with task messages
final_message = f"{message_task_1}\n" + "\n".join(task_messages)

# print(final_message)

subject = "Data Quality Check for Source"

alert_quality.send_email(
    body= f"""Subject: {subject}

{final_message}. 

Please review the attached report and fix the error.""",

    to_email="20520270@gm.uit.edu.vn",

    password=password
)
