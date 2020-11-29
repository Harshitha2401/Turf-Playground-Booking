import mysql.connector
from mysql.connector import Error
import pandas as pd
import datetime

def slot_booking(data,connection,loc,game):
    booking_date=datetime.date.today()
    slot_details = (data.columns.values[1:])
    print("********AVAILABLE SLOTS********")
    valid_slot=[]
    for i, j in enumerate(slot_details, start=1):
        if data[j][0] == 'Slot Available':
            valid_slot.append(i)
            print("Press", i, "to book", j)
    slot = int(input("Enter the slot need to be booked:"))
    if slot not in valid_slot:
        print("OOPS!! Invalid Slot selected\nNo slot Booked,TRY AGAIN")
    else:
        user_name=input("Enter the Username:")
        user_mail=input("Enter the mail-id for communication:")
        sql_insert=f"INSERT INTO Booking_Details(Location,Slot,Game,Booking_Date,user_name,user_mail_id) VALUES ('{loc}','{slot_details[slot-1]}','{game}','{booking_date}','{user_name}','{user_mail}')"
        cursor=connection.cursor()
        cursor.execute(sql_insert)
        cursor.execute("Commit")
        print(f"Request to book the slot {slot_details[slot-1]} has been Accepted!\nCheck your provided mail id for confirmation")

def display_slot(connection,loc):
    game=input("Enter the game for which you need to view the slots:")
    game=game.lower()
    if game=='cricket':
        data=pd.read_sql_query("select * from cricket where Location=%s",connection,params=(loc,))
        slot_booking(data,connection,loc,game)
    elif game=='badminton':
        data = pd.read_sql_query("select * from badminton where Location=%s", connection, params=(loc,))
        slot_booking(data,connection,loc,game)
    elif game=='8_ball_pool':
        data=pd.read_sql_query("select * from 8_ball_pool where Location=%s",connection,params=(loc,))
        slot_booking(data,connection,loc,game)
    elif game=='tt':
        data=pd.read_sql_query("select * from tt where Location=%s",connection,params=(loc,))
        slot_booking(data,connection,loc,game)
    else:
        print("OOPS!!Invalid Game Selected")
        exit(0)






