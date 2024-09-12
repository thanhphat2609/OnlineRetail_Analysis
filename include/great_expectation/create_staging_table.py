# bash test connect
# python test_connect.py 'server_name' 'Online_Retail' 'adminsql' 'Thanhphat2609@'

import sys
import pandas as pd
import pyodbc
from airflow.models import Variable


sys.path.append("/usr/local/airflow/include/great_expectation")

server = Variable.get("my_server")
database = Variable.get("my_database")
username = Variable.get("my_username")
password = Variable.get("my_password")


from interact_db import *
interact = interact_db()

try:
    connection = interact.connect_mssql(database, server, username, password)
    # print("Connection Successfully!!!")

    try:
        print("Create table with data Successfully!!!")
    except Exception as e:
        print("Error while create table with data for Staging Phase")

except Exception as e:
    print("Connection Failed by: ", e)
