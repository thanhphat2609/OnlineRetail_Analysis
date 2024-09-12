from datetime import datetime
import sys
import pandas as pd
import pyodbc
from sqlalchemy import create_engine
from airflow.models import Variable


sys.path.append("/usr/local/airflow/include/great_expectation")

server = Variable.get("my_server")
database = Variable.get("my_database")
username = Variable.get("my_username")
password = Variable.get("my_password")


from interact_db import *
interact = interact_db()

try:
    connection, connectionString = interact.connect_mssql(database, server, username, password)
    # Create SQLAlchemy engine
    engine = create_engine(connectionString)
    # print("Connection Successfully!!!")

    path_stg = "/usr/local/airflow/include/dataset/Online_Retail.csv"

    # Using different encodings for dataset
    try:
        df = pd.read_csv(path_stg, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(path_stg, encoding='ISO-8859-1')
        except UnicodeDecodeError:
            df = pd.read_csv(path_stg, encoding='cp1252')

    # print(df)
    try:    
        # Create table name by pattern: "retail_sales_2024_09_19"
        schema_name = "STG"
        executionDate = datetime.now().strftime("%Y_%m_%d")
        table_name = f"{schema_name}.retail_sales_{executionDate}"

        # Create table in STG schema
        df.to_sql(name=table_name, con=engine, schema=schema_name, if_exists='replace', index=False)

        print(f"Processing: {executionDate} for staging phase of table {table_name} successfully!!!")
        
    except Exception as e:
        print("Error while create table with data for Staging Phase")

except Exception as e:
    print("Connection Failed by: ", e)
