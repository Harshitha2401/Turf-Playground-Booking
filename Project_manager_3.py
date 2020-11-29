import mysql.connector
from mysql.connector import Error
import pandas as pd
import datetime
import Project_manager_5

def slot_check_update(connection,cursor,loc):
    pd.set_option("display.max_rows", 100, "display.max_columns", 100)
    pd.set_option("display.expand_frame_repr", False)
    output = pd.read_sql_query("SELECT * FROM booking_details WHERE Location=%s", connection,params=(loc,))
    if not output.empty:
        for i in range(len(output)):
            query = (f"UPDATE {output.iloc[i]['Game']} SET {output.iloc[i]['Slot']}='{output.iloc[i]['Booking_Date']}' WHERE Location='{loc}'")
            cursor.execute(query)
            cursor.execute("COMMIT")
            Project_manager_5.send_mail(output.iloc[i]['user_name'],output.iloc[i]['user_mail_id'])
            cursor.execute("DELETE FROM booking_details WHERE Location=%s",(loc,))
            cursor.execute("COMMIT")

        print("ALL SLOT BOOKING REQUESTS ARE PROCESSED!!!!")
    else:
        print("NO REQUESTS ARE PENDING!")






