from datetime import datetime
import sys
import pandas as pd
from airflow.models import Variable
import subprocess

import pyodbc

from interact_db import *
interact = interact_db()

# Verify SQL Server Credentials
server = Variable.get("my_server")
database = Variable.get("my_database")
username = Variable.get("my_username")
password = Variable.get("my_password")

try:
    connection, connectionString = interact.connect_mssql(server, database, username, password)
    # Create SQLAlchemy engine
    cursor = connection.cursor()  

    path_stg = "/usr/local/airflow/include/dataset/Online_Retail.csv"

    # Using different encodings for reading raw_dataset
    try:
        df = pd.read_csv(path_stg, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(path_stg, encoding='ISO-8859-1')
        except UnicodeDecodeError:
            df = pd.read_csv(path_stg, encoding='cp1252')

    # Handle some exception
    df = df.replace({pd.NA: None})

    
    df['UnitPrice'] = df['UnitPrice'].round(2)

    # print(df)
    try:    
        # Create table name by pattern: "retail_sales_2024_09_19"
        # executionDate = datetime.now().strftime("%Y_%m_%d")
        # executionDate = "2024_09_05"
        table_name = f"retail_sales"

        DROP_TABLE_QUERY = "DROP TABLE IF EXISTS STG.{table_name}"
        cursor.execute(DROP_TABLE_QUERY)
        connection.commit()


        # Create table in STG schema
        CREATE_TABLE_QUERY = f"""
                    CREATE TABLE STG.{table_name}(
                        InvoiceNo VARCHAR(1000),
                        StockCode VARCHAR(1000),
                        Description VARCHAR(1000),
                        Quantity INT,
                        InvoiceDate VARCHAR(100),
                        UnitPrice DECIMAL(10, 2), 
                        CustomerID INT,
                        Country VARCHAR(1000)
                    )
                """
        cursor.execute(CREATE_TABLE_QUERY)
        connection.commit()
        
        # print(f"Create Staging table {table_name} Successfully!!")

        # Insert data into STG table
        INSERT_QUERY = f"""
                            INSERT INTO STG.{table_name} 
                            (InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        """

        for index, row in df.iterrows():
            cursor.execute(INSERT_QUERY, row['InvoiceNo'], row['StockCode'], row['Description'], row['Quantity'], 
                        row['InvoiceDate'], row['UnitPrice'], row['CustomerID'], row['Country'])

        connection.commit()
        cursor.close()

        # print(f"Processing: {executionDate} for staging phase of table {table_name} successfully!!!")

    except Exception as e:
        print("Error while create table with data for Staging Phase: ", e)

except Exception as e:
    print("Connection Failed by: ", e)
