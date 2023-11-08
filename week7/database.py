# import sqlite3
# conn = sqlite3.connect('database.db')
# cur = conn.cursor()
# rows = cur.execute("SELECT * FROM users")
# for row in rows:
#     print(row)
# conn.close()

# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root"
)

print(mydb)
