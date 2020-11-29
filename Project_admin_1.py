import mysql.connector
from mysql.connector import Error
import Project_admin_2

def create(cursor):
    mysql_database = 'CREATE DATABASE IF NOT EXISTS ADMIN'
    cursor.execute(mysql_database)
    print("Database created")
    cursor.execute('USE ADMIN')
    mysql_table = """CREATE TABLE IF NOT EXISTS Manager (Manager_Name varchar(255),
                                           username varchar(255) PRIMARY KEY,
                                           Password varchar(255),
                                           Password_Type varchar(255) DEFAULT 'Default',
                                           Email_ID varchar(255),
                                           Location varchar(255)) """


    mysql_location = """CREATE TABLE IF NOT EXISTS Location (Location_Name varchar(255) PRIMARY KEY,
                                                            Sports_1 varchar(255) DEFAULT 'Cricket',
                                                            Sports_1_price INT,
                                                            Sports_2 varchar(255) DEFAULT '8_Ball_Pool',
                                                            Sports_2_price INT,
                                                            Sports_3 varchar(255) DEFAULT 'Badminton',
                                                            Sports_3_price INT,
                                                            Sports_4 varchar(255) DEFAULT 'TT',
                                                            Sports_4_price INT)"""

    mysql_table_cricket = """CREATE TABLE IF NOT EXISTS Cricket ( 
                                               Location varchar(255)  references Location(Location_Name),
                                               Slot_1_9AM_12PM varchar(255) DEFAULT 'Slot Available',
                                               Slot_2_12PM_3PM varchar(255) DEFAULT 'Slot Available',
                                               Slot_3_3PM_6PM varchar(255) DEFAULT 'Slot Available',
                                               Slot_4_6PM_9PM varchar(255) DEFAULT 'Slot Available',
                                               PRIMARY KEY(Location))"""
    mysql_table_8_Ball_Pool = """CREATE TABLE IF NOT EXISTS 8_Ball_Pool ( 
                                                   Location varchar(255)  references Location(Location_Name),
                                                   Slot_1_9AM_12PM varchar(255) DEFAULT 'Slot Available',
                                                   Slot_2_12PM_3PM varchar(255) DEFAULT 'Slot Available',
                                                   Slot_3_3PM_6PM varchar(255) DEFAULT 'Slot Available',
                                                   Slot_4_6PM_9PM varchar(255) DEFAULT 'Slot Available',
                                                   PRIMARY KEY(Location)) """
    mysql_table_Badminton = """CREATE TABLE IF NOT EXISTS Badminton ( 
                                                       Location varchar(255) references Location(Location_Name),
                                                       Slot_1_9AM_11AM varchar(255) DEFAULT 'Slot Available',
                                                       Slot_2_11AM_1PM varchar(255) DEFAULT 'Slot Available',
                                                       Slot_3_1PM_3PM varchar(255) DEFAULT 'Slot Available',
                                                       Slot_4_3PM_5PM varchar(255) DEFAULT 'Slot Available',
                                                       Slot_5_5PM_7PM varchar(255) DEFAULT 'Slot Available',
                                                       Slot_6_7PM_9PM varchar(255) DEFAULT 'Slot Available',
                                                       PRIMARY KEY(Location)) """
    mysql_table_TT = """CREATE TABLE IF NOT EXISTS TT ( 
                                                       Location varchar(255)  references Location(Location_Name),
                                                       Slot_1_9AM_11AM varchar(255) DEFAULT 'Slot Available',
                                                       Slot_2_11AM_1PM varchar(255) DEFAULT 'Slot Available',
                                                       Slot_3_1PM_3PM varchar(255) DEFAULT 'Slot Available',
                                                       Slot_4_3PM_5PM varchar(255) DEFAULT 'Slot Available',
                                                       Slot_5_5PM_7PM varchar(255) DEFAULT 'Slot Available',
                                                       Slot_6_7PM_9PM varchar(255) DEFAULT 'Slot Available',
                                                       PRIMARY KEY(Location)) """
    mysql_booking_details="""CREATE TABLE IF NOT EXISTS Booking_Details(
                                                                        Location varchar(255)  references Location(Location_Name),
                                                                        Slot varchar(255),
                                                                        Game varchar(255),
                                                                        Booking_Date date,
                                                                        user_name varchar(255),
                                                                        user_mail_id varchar(255))"""

    

    queries=[mysql_table,mysql_location,mysql_table_cricket,mysql_table_Badminton,mysql_table_8_Ball_Pool,mysql_table_TT,mysql_booking_details]
    for i in queries:
        cursor.execute(i)
    cursor.execute("ALTER TABLE Manager ADD FOREIGN KEY (Location) references Location(Location_Name)")


try:
    connection = mysql.connector.connect(host='localhost', username='root', password='root')
    cursor = connection.cursor()

except Error as e:
    print(e)


create(cursor)
Project_admin_2.location_insertion(cursor)
Project_admin_2.values(cursor)
Project_admin_2.games_insertion(cursor)

cursor.close()
connection.close()
