# Streaming Data Pipelines V1



<p align='center'>
<img width="732" alt="image" src="https://github.com/rickichann/streaming_data_pipelines_v1/assets/53082147/69260da3-6c57-40e4-af60-15bf648d5131">
</p>

  
 
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
<img width="967" alt="image" src="https://github.com/rickichann/streaming_data_pipelines_v1/assets/53082147/c4a1d07a-c31b-44a7-811c-46a1dac21056">

- conf_source : source database configuration.
- conf_destination : destination database configuration.
- source_table_name : table name *source db.
- destination_table_name : table name *destination db.
- unique_constraint_column : the unique column is usually the primary key.
- sync_date : column used to store time information when data is inserted or data changes occur

Notes :
Convert notebook (.ipynb) to .py file
```
jupyter nbconvert --to script 'streaming_data_pipelines_v1.ipynb'
```
