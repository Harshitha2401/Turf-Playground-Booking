import mysql.connector
from mysql.connector import Error
import Project_User_2

connection=mysql.connector.connect(host="localhost",username="root",password="root")
cursor=connection.cursor()
cursor.execute("USE admin")

input_location=input("Enter the name of the location:")
cursor.execute("SELECT Location_Name FROM Location")
existing_location=cursor.fetchall()
for loc in existing_location:
    if input_location in loc:
        Project_User_2.rates(connection, cursor, input_location)
        break

else:
    print("Entered Location does'nt exist")