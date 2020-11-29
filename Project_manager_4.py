import mysql.connector
from mysql.connector import Error
import pandas as pd
import datetime

def slot_change(connection,cursor,game,loc):
    pd.set_option("display.max_rows", 100, "display.max_columns", 100)
    pd.set_option("display.expand_frame_repr", False)
    slot_check_query=f"SELECT * FROM {game} WHERE Location='{loc}'"
    slot_check = pd.read_sql_query(slot_check_query, connection)
    for row in slot_check:
        if row != 'Location':
            for i in slot_check[row]:
                if i != 'Slot Available' and i < datetime.date.strftime(datetime.date.today(), '%Y-%m-%d'):
                    query = f"UPDATE {game} SET {row}='Slot Available' WHERE Location='{loc}'"
                    cursor.execute(query)
                    cursor.execute("COMMIT")

def game_select(connection,cursor,loc):
    games=['cricket','tt','badminton','8_ball_pool']
    for game in games:
        slot_change(connection,cursor,game,loc)
    print("SLOTS CHECKING/UPDATION is completed!")


