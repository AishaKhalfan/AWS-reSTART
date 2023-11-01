# Insert, Update, and Delete Data in a Database
 

## Scenario
The database operations team has created a relational database called world containing three tables: city, country, and countrylanguage. You have to validate the configuration of the database by running INSERT, UPDATE, and DELETE statements on the country table.  

 

## Lab overview and objectives
This lab demonstrates how to insert, update, delete, and import rows of data using structured query language (SQL).

After completing this lab, you will be able to:

- Insert rows into a table
- Update rows in a table
- Delete rows from a table
- Import rows from a database backup file

When you start this lab, the following resources are already created for you:
![img]()
A Command Host instance and world database containing three tables

At the end of this lab, your architecture will look like the following example:
![img]()
 lab user is connected to a database instance. Insert, Update, and Delete operations are shown.

Sample data in this course is taken from Statistics Finland, general regional statistics, February 4, 2022.

# Duration
This lab requires approximately **45 minutes** to complete.

## AWS service restrictions
In this lab environment, access to AWS services and service actions might be restricted to the ones that you need to complete the lab instructions. You might encounter errors if you attempt to access other services or perform actions beyond the ones that this lab describes.

 
###  Accessing the AWS Management Console
1. At the upper-right corner of these instructions, choose  Start Lab 

Troubleshooting tip: If you get an Access Denied error, close the error box, and choose  Start Lab again.

2. The following information indicates the lab status:

- A red circle next to AWS  at the upper-left corner of this page indicates the lab has not been started.
- A yellow circle next to AWS  at the upper-left corner of this page indicates the lab is starting.
- A green circle next to AWS  at the upper-left corner of this page indicates the lab is ready.
Wait for the lab to be ready before proceeding.

3. At the top of these instructions, choose the green circle next to AWS 

This option opens the AWS Management Console in a new browser tab. The system automatically sign you in.

Tip: If a new browser tab does not open, a banner or icon at the top of your browser will indicate that your browser is preventing the site from opening pop-up windows. Choose the banner or icon, and choose Allow pop-ups.

4. Arrange the AWS Management Console tab so that it displays along side these instructions. Ideally, you should be able to see both browser tabs at the same time so that you can follow the lab steps.

 **Do not change the lab Region unless specifically instructed to do so.**

 

# Task 1: Connect to a database
In this task, you connect to an instance containing a database client, which is used to connect to a database. This instance is referred to as the Command Host.

5. In the AWS Management Console, choose the  Services menu. Under Compute, choose EC2.

6. In the left navigation pane, choose Instances.

7. Next to the instance labelled Command Host, select the check box  and then choose Connect.

Note: If you do not see the Command Host, the lab is possibly still being provisioned, or you may be using another Region.

8. For Connect to instance, choose the Session Manager tab.

9. Choose Connect to open a terminal window.

Note: If the Connect button is not available, wait for a few minutes and try again.

10. To configure the terminal to access all required tools and resources, run the following command:
```bash
sudo su
cd /home/ec2-user/
```
** Tips:**

- Copy and paste the command into the Session Manager terminal window.
- If you are using a Windows system, press Shift+Ctrl+v to paste the command.
11. To connect to the database instance, run the following command in the terminal. A password was configured when the database was installed.

```SQL
mysql -u root --password='re:St@rt!9'
```
 The MySQL command-line client is a SQL shell that you can use to interact with database engines.

| Switch | Description |
| --- | ----------- |
| -u or --user | The MySQL user name used to connect to a database instance |
| -p or --password | The MySQL password used to connect to a database instance |
  **Tip:** At any stage of the lab, if the Sessions Manager window is not responsive or if you need to reconnect to the database instance, then follow these steps:

- Close the Sessions Manager window, and try to reconnect using the previous steps.
- Run the following commands in the terminal.

```bash
sudo su
cd /home/ec2-user/
mysql -u root --password='re:St@rt!9'
```
12. To show the existing databases, enter the following command in the terminal. Make a note of the currently available databases.

```SHOW DATABASES;```

 

## Task 2: Insert data into a table
In this task, you insert sample data into the country table.

13. To verify that the **country** table is empty, run the following command. The SELECT statement is used to identify the columns that should be included in the result set. The use of the * denotes all columns. The FROM clause is used in the following example to specify the database and table that is queried.

```SQL
SELECT * FROM world.country;
```
The table should be empty because it was just created.

14. To insert rows into the **country** table, run the following commands. The values in the VALUES clause need to be in the same order as defined by the table schema. 

```SQL
INSERT INTO world.country VALUES ('IRL','Ireland','Europe','British Islands',70273.00,1921,3775100,76.8,75921.00,73132.00,'Ireland/Éire','Republic',1447,'IE');

INSERT INTO world.country VALUES ('AUS','Australia','Oceania','Australia and New Zealand',7741220.00,1901,18886000,79.8,351182.00,392911.00,'Australia','Constitutional Monarchy, Federation',135,'AU');
```
15. To verify that two rows were successfully inserted into the country table, run the following query.

```SQL
SELECT * FROM world.country;
```
The table should now contain two rows and should appear as follows.

|Code | Name | Continent | Region | SurfaceArea	| IndepYear | Population | LifeExpectancy | GNP | GNPOld | LocalName | GovernmentForm | Capital | Code2 |
| -------- | ------- | -------- | ------- |-------- | ------- | -------- | ------- | -------- | ------- |-------- | ------- |-------- |-------- |
|AUS | Australia | Oceania | Australia and New Zealand | 7741220 | 1901	| 18886000 | 79.8 | 351182 | 392911 | Australia	| Constitutional Monarchy, Federation |	135 | AU |
|IRL | Ireland | Europe | British Islands | 70273 | 1921 | 3775100 | 76.8 | 75921 | 73132 | Ireland/Éire | Republic | 1447 | IE |
 

## Task 3: Update rows in a table
In this task, you update both rows in the country table using an UPDATE statement.

16. To set the value in the **Population** column to 0 for both rows in the country table, run the following UPDATE statement. 

```SQL
UPDATE world.country SET Population = 0;
```
All rows are updated because the UPDATE statement does not include a WHERE condition. A WHERE clause uses conditions to filter rows returned by a query. The next lab introduces the WHERE clause.

17. To verify that the **Population** column in the country table was updated, run the following command.

```SQL
SELECT * FROM world.country;
```
18. To update the **Population** and **SurfaceArea** columns for all rows in the country table, run the following UPDATE statement.

```SQL
UPDATE world.country SET Population = 100, SurfaceArea = 100;
```
19. To verify that the Population and SurfaceArea columns in the country table were updated, run the following command.

```SQL
SELECT * FROM world.country;
```
 

## Task 4: Delete rows from a table
In this task, you delete both rows in the country table using a DELETE statement. 

Exercise caution when using data manipulation statements such as UPDATE and DELETE because these changes may not be reversible. 

20. To delete ALL rows from the country table, run the following command. 

```SQL
DELETE FROM world.country;
```
Because the DELETE statement does not include a WHERE condition, all rows are deleted.

21. To verify that all rows have been deleted from the country table, run the following command.

```SQL
SELECT * FROM world.country;
```
 

## Task 5: Import data using an SQL file
In this task, you import sample data into the country table using an SQL file.

22. To exit the MySQL terminal, run the following command.

``QUIT;``
23. To verify that the **world.sql** file has been downloaded, run the following command.

```BASH
ls /home/ec2-user/world.sql
```

Recall Linux commands
24. It is time-consuming to insert individual rows into a table. You can create a SQL script file containing a group of SQL statements to quickly load data into a database. To load rows into the country table, run the following command.

```BASH
mysql -u root --password='re:St@rt!9' < /home/ec2-user/world.sql
```
This database file adds two additional tables and inserts data into all three tables.

25. To reconnect to the database, run the following command.

```BASH
mysql -u root --password='re:St@rt!9'
```
26. To verify that the script ran successfully, run the following command.
```SQL
USE world;
SHOW TABLES;
```
Observe that there are three tables named city, country, and countrylanguage.

27. To verify that the rows were loaded successfully, run the following command.

```SQL
SELECT * FROM country;
```
Notice that there are more entries in the country table.

28. Similarly, use the SELECT statement to query the city and countrylanguage tables that were created when you imported the backup file.
 

## Conclusion
:thumbsup: Congratulations! You now have successfully:

- Inserted rows into a table
- Updated rows in a table
- Deleted rows from a table
- Imported rows from a database backup file
 

## Lab complete 
Choose  End Lab at the top of this page, and then select Yes to confirm that you want to end the lab.
An Ended AWS Lab Successfully message is briefly displayed indicating that the lab has ended.
 

Additional resources
Country, city, and language data, Statistics Finland: The material was downloaded from Statistics Finland's interface service on February 4, 2022, with the license CC BY 4.0. The original data source is available from Statistics Finland.

- For more information about database functions and operators, see the following resources:

	- [INSERT statement](https://mariadb.com/kb/en/insert/)
	- [UPDATE statement](https://mariadb.com/kb/en/update/)
	- [DELETE statement](https://mariadb.com/kb/en/delete/)
