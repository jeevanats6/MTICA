def printDay(dn):
    if(dn==1):
        return 'Sunday'
    elif(dn==2):
        return 'Monday'
    elif(dn==3):
        return 'Tuesday'
    elif(dn==4):
        return 'Wednesday'
    elif(dn==5):
        return 'Thursday'
    elif(dn==6):
        return 'Friday'
    elif(dn==7):
        return 'Saturday'
    
    else:
        return 'invalid'
    

for i in range(3):
    inpNum=int(input())
    print(printDay(inpNum))



