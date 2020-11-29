import mysql.connector
from mysql.connector import Error
import Project_User_2
import Project_manager_2
import Project_manager_3
import Project_manager_4

connection=mysql.connector.connect(host='localhost',username='root',password='root')
cursor=connection.cursor()
cursor.execute("USE admin")

username=input("Enter the Username:")

cursor.execute("SELECT username,password FROM manager")
result=cursor.fetchall()

for i in result:
    if i[0] == username:
        password = input("Enter the Password:")
        if i[1] == password:
            print("Login Successful!!!!")
            Project_manager_2.password_change(connection,cursor,username,password)
            cursor.execute("SELECT Location FROM manager WHERE username=%s",(username,))
            loc=cursor.fetchone()[0]
            Project_manager_4.game_select(connection, cursor,loc)
            Project_manager_3.slot_check_update(connection,cursor,loc)
            exit(0)
        else:
            print("Invalid Password")
            exit(0)
    else:
        continue
else:
    print("Invalid Username")
