
import mysql.connector;

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="welcome"
)

print(mydb)

print("DB connection successfully completed")