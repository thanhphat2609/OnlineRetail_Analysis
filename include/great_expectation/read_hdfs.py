import pandas as pd
from hdfs import InsecureClient
import os

# To connect to WebHDFS by providing the IP of the HDFS host and the WebHDFS port.
client_hdfs = InsecureClient('http://hdfs-namenode:9870', user='thanhphat')

with client_hdfs.read('/Online_Retail_Analysis/datalake/online_retail.csv', encoding = 'ISO-8859-1') as reader:
  df = pd.read_csv(reader,index_col=0)

print(df)