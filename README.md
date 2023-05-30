# streaming_data_pipelines_v1

1. Run this query !, to add a unique constraint on unique columns:
```
ALTER TABLE transaction_table ADD CONSTRAINT constraint_transaction_table UNIQUE (transaction_id);
```


2. Fill in the following variables !

```
conf_source = 'mysql+pymysql://username:password@ipaddress:port/dbname'
conf_destination = 'postgresql://username:password@ipaddress:port/dbname'
source_table_name = 'table_name'
destination_table_name = 'wh_transaction_table'
unique_constraint_column = 'transaction_id'
sync_date = 'write_date' #dtu, write_date  
```

3. For the first time running the pipeline, change the write_date manually (according to the data you want to retrieve), and when finished, change it back to the beginning.
![image](https://github.com/rickichann/streaming_data_pipelines_v1/assets/53082147/bb8ea9fb-2e6f-43de-a8a4-ba22667c089b)

- conf_source : source database configuration.
- conf_destination : destination database configuration.
- source_table_name : table name *source db.
- destination_table_name : table name *destination db.
- unique_constraint_column : the unique column is usually the primary key.
- sync_date : column used to store time information when data is inserted or data changes occur
