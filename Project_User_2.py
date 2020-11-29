import mysql.connector
from mysql.connector import Error
import numpy as np
import pandas as pd
import Project_User_3

def rates(connection,cursor,loc):
    pd.set_option("display.max_rows",100,"display.max_columns",100)
    pd.set_option("display.expand_frame_repr",False)
    location_details=pd.read_sql("select * from location where Location_Name=%s",connection,params=(loc,))
    print("*"*25,"Details of Games and their price available in",loc,"Sports Club","*"*25)
    print(location_details)

    Project_User_3.display_slot(connection, loc)



