def printMonth(dn):
    if(dn==1):
        return 'january'
    elif(dn==2):
        return 'feb'
    elif(dn==3):
        return 'march'
    elif(dn==4):
        return 'April'
    elif(dn==5):
        return 'may'
    elif(dn==6):
        return 'jun'
    elif(dn==7):
        return 'july'
    elif(dn==8):
        return 'august'
    elif(dn==9):
        return 'sep'
    elif(dn==10):
        return 'oct'
    elif(dn==11):
        return 'November'
    elif(dn==12):
        return 'December'
    else:
        return 'invalid'
    

for i in range(3):
    inpNum=int(input())
    print(printMonth(inpNum))



