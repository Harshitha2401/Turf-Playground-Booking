def password_check(pwd):
    ucount=lcount=dcount=scount=0
    if len(pwd)<6 or len(pwd)>16:
        return False
    else:
        for i in pwd:
            if i.isupper():
                ucount+=1
            elif i.islower():
                lcount+=1
            elif i.isdigit():
                dcount+=1
            elif i in ['#','@','_']:
                scount+=1
            else:
                return False
        if ucount>=1 and lcount>=1 and dcount>=1 and scount>=1:
            return True
        else:
            return False