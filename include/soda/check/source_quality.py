import requests
import time
import sys
import pandas as pd
from datetime import datetime
from hdfs import InsecureClient

# Soda Cloud account 
soda_cloud_url = 'cloud.us.soda.io' # cloud.us.soda.io (US Customers) or cloud.soda.io (EU Customers)
soda_apikey = '711a0dfc-747f-4d3b-b207-4d4872550d8e' # Soda Cloud API key ID 
soda_apikey_secret = 'vgDI4KjeVpIvuo6mySn8Zuy0SfZEdTb1iO1Aeg0Cwg6rL1uv4DOUa' # Soda Cloud API key secret

# HDFS configuration
hdfs_url = 'hdfs://hdfs-namenode:9000'  # Replace with your HDFS URL
hdfs_client = InsecureClient(hdfs_url)


# Check exist file
def check_hdfs_file(file_path):
    """Check if a file exists in HDFS."""
    try:
        return hdfs_client.status(file_path, strict=False) is not None
    except Exception as e:
        print(f"Error checking file {file_path}: {e}")
        return False

# Run all check
file_path = 'hdfs://hdfs-namenode:9000/Online_Retail_Analysis/datalake/online_retail.csv'  # Replace with the path to the file you want to check
if check_hdfs_file(file_path):
    print(f"File {file_path} exists in HDFS.")
else:
    print(f"File {file_path} does not exist in HDFS.")
