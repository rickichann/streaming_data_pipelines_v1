# streaming_data_pipelines_v1

1. Run this query :
```
ALTER TABLE transaction_table ADD CONSTRAINT constraint_transaction_table UNIQUE (transaction_id);
```


2. Fill in the following variables !

```
conf_source = 'mysql+pymysql://username:password@ipaddress:port/dbname'
conf_destination = 'postgresql://username:password@ipaddress:port/dbname'
table_name = 'table_name'
unique_constraint_column = 'transaction_id'
sync_date = 'write_date' #dtu, write_date  ```



Notes
