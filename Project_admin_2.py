import random
import string
import Project_admin_3

def games_insertion(cursor):
    cursor.execute("INSERT IGNORE into Cricket (Location) values ('ITPL')")
    cursor.execute("INSERT IGNORE into Cricket (Location) values ('Indiranagar')")
    cursor.execute("INSERT IGNORE into Cricket (Location) values ('Whitefield')")
    cursor.execute("INSERT IGNORE into 8_Ball_Pool (Location) values ('Whitefield')")
    cursor.execute("INSERT IGNORE into 8_Ball_Pool (Location) values ('Indiranagar')")
    cursor.execute("INSERT IGNORE into 8_Ball_Pool (Location) values ('ITPL')")
    cursor.execute("INSERT IGNORE into Badminton (Location) values ('Whitefield')")
    cursor.execute("INSERT IGNORE into Badminton (Location) values ('Indiranagar')")
    cursor.execute("INSERT IGNORE into Badminton (Location) values ('ITPL')")
    cursor.execute("INSERT IGNORE into TT (Location) values ('Whitefield')")
    cursor.execute("INSERT IGNORE into TT (Location) values ('ITPL')")
    cursor.execute("INSERT IGNORE into TT (Location) values ('Indiranagar')")
    cursor.execute("Commit")

def location_insertion(cursor):
    cursor.execute("INSERT IGNORE into Location (Location_Name,Sports_1_price,Sports_2_price,Sports_3_price,Sports_4_price) values ('ITPL',1200,800,500,400)")
    cursor.execute("INSERT IGNORE into Location (Location_Name,Sports_1_price,Sports_2_price,Sports_3_price,Sports_4_price) values ('Whitefield',1000,600,400,700)")
    cursor.execute("INSERT IGNORE into Location (Location_Name,Sports_1_price,Sports_2_price,Sports_3_price,Sports_4_price) values ('Indiranagar',1500,550,750,600)")

def randomStringwithDigits(stringLength=10):
    password_characters=string.ascii_letters+string.digits+'_@#'
    return ''.join(random.choice(password_characters) for i in range(stringLength))

def insertion(cursor,Manager_Name,username,Password,Email_ID,Location):
    if Project_admin_3.send_mail(Manager_Name,username,Password,Email_ID):
        mysql_insert = """INSERT IGNORE into Manager (Manager_Name,username,Password,Email_ID,Location) VALUES (%s,%s,%s,%s,%s)"""
        record=(Manager_Name,username,Password,Email_ID,Location)
        cursor.execute(mysql_insert,record)
        cursor.execute("Commit")


def values(cursor):
    while True:
        Manager_Name=input("Enter the manager name:")
        username=input("Enter the username:")
        Password=randomStringwithDigits()
        Email_ID=input("Enter the email-id:")
        Location=input("Enter the location:")
        insertion(cursor,Manager_Name,username,Password,Email_ID,Location)
        ch=input("Any more record to be inserted:(Y/N)")
        if ch=='N' or ch=='n':
            return



