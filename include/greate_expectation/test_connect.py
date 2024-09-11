# bash test connect
# python test_connect.py 'server_name' 'Online_Retail' 'adminsql' 'Thanhphat2609@'

import sys
import pandas as pd

sys.path.append("/usr/local/airflow/include/greate_expectation")

database = sys.argv[1]
server = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]

from interact_db import *
interact = interact_db()

try:
    connection = interact.connect_mssql(database, server, username, password)
except Exception as e:
    print("Connection Failed by: ", e)
