#!/usr/bin/env python
# coding: utf-8

# In[415]:


import pandas as pd
import datetime as dt
from sqlalchemy import create_engine
import sys


# In[416]:


_start = dt.datetime.now()
dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 


# In[417]:


def pipeline_peformance(x):
    _end = dt.datetime.now()
    difference = _end - x
    x_ms = str(round(difference.total_seconds() * (10 ** 3),2)) + ' ms'
    print(x_ms)


# In[418]:


conf_source = 'mysql+pymysql://username:password@ipaddress:port/dbname'
conf_destination = 'postgresql://username:password@ipaddress:port/dbname'
source_table_name = 'transaction_table'
destination_table_name = 'wh_transaction_table'
unique_constraint_column = 'transaction_id'
sync_date = 'write_date' #dtu, write_date  


# In[419]:


# source
con_source = create_engine(conf_source)

# destination
connect_dest = create_engine(conf_destination)
con_dest = connect_dest.connect()


# In[420]:


# last write_date
last_write_date = con_dest.execute('SELECT MAX(write_date) FROM {}'.format(destination_table_name)).scalar()
ld = "'"+str(last_write_date)+"'"


# In[421]:


df = pd.read_sql_query(''' 

    SELECT 
    
    *
    
    FROM {}
    WHERE {} >= {}
    
'''.format(source_table_name,sync_date,ld),con_source)

# drop_columns (optional)
df.drop(columns=['id'],inplace=True)


# In[422]:


# stop
if len(df) == 1:
    pipeline_peformance(_start)
    sys.exit()


# In[423]:


# # error handling (optional)
# - 
# - 
# - 
# - 


# In[ ]:


df.head()


# In[429]:


table_str = tuple(df.columns)
excluded_str = list(map(lambda i, j: str(i) + '=' + "EXCLUDED." + str(j), df.columns, df.columns))
excluded_str = str(excluded_str)[1:-1]
s_str = '('+str(len(df.columns) * '%s,')[:-1]+')'

xx=0
for row in df.itertuples(index=False):
    con_dest.execute('''INSERT INTO {}{} VALUES{} ON CONFLICT ({})
                             DO
                             UPDATE
                             SET{}
                             
                             '''.format(destination_table_name,table_str,s_str,unique_constraint_column,excluded_str).replace("'"," "),
                          (row))
    xx += 1
print('Query OK, {} row affected'.format(xx))


# In[428]:


pipeline_peformance(_start)


# In[ ]:




