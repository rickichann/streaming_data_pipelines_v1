import polars as pl
import psycopg2
import os

CONNECTION_URI = 'postgresql://<username>:<password>@<ipaddress>:<port>/<dbname>' 
years = [2019,2020,2021,2022,2023] 
# save to 
table_name = 'product_cummulative'

# conn_src = psycopg2.connect(CONNECTION_URI)
# cur_src = conn_src.cursor()
# cur_src.execute("DELETE FROM product_cummulative")
# conn_src.commit()
# print("The data has been purged")

def product_cummulative(query,conn,years):
    connection_uri = conn
    query = query.format(years)
    
    data = pl.read_database(query=query, connection_uri=connection_uri) 
    data = data.with_columns(pl.lit(years).alias('years'))
    return data


query = ''' SELECT
                *
                FROM table_name
                WHERE EXTRACT(year FROM transaction_date) = '{}'
                '''

for i in years:
    product_cummulative(query,CONNECTION_URI,i).write_parquet('./parquet_data/product_cummulative/program_{}.parquet'.format(i))

# read_parquet
folder_path = './parquet_data/product_cummulative'
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.parquet')]
df = pl.DataFrame()

for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df_temp = pl.read_parquet(file_path)
    df = pl.concat([df, df_temp])

df.write_database('{}'.format(table_name), CONNECTION_URI,if_exists='replace')
print("201 Created", "{}".format(table_name))
print("Total rows inserted: ",len(df))