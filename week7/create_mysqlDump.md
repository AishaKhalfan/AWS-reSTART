# How to create and retrieve mysql database dump

1. mysqldump -u username -p world > world_dump.sql
2. mysql -u username -p new_database < world_dump.sql

