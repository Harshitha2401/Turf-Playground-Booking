import pandas as pd
import Password_Check

def password_change(connection,cursor,username,password):
    pd.set_option("display.max_rows",100,"display.max_columns",100)
    pd.set_option("display.expand_frame_repr",False)
    check=pd.read_sql("select * from manager where username=%s",connection,params=(username,))
    if check["Password_Type"][0]=="Default":
        print("First Time Login!!\nKindly reset the default password")
        old_password=input("Enter the existing password:")
        new_password=input("Enter the new password:")
        re_new_password=input("Re-Enter the password:")
        if old_password==check["Password"][0]:
            if new_password==re_new_password:
                if Password_Check.password_check(new_password):
                    pwd_update=f"""update manager set Password='{new_password}',Password_Type='Updated' where username='{username}'"""
                    cursor.execute(pwd_update)
                    cursor.execute("Commit")
                    print("Password changed Successfully!\nLogin with new password to proceed")
                    exit(0)
                else:
                    print("Password Criteria not matching")
                    exit(0)
            else:
                print("Password Not matching")
                exit(0)
        else:
            print("OOPS!!!Incorrect Password Entered")
            exit(0)

