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
    





def printDay1(dn):
   mn=''
   if(dn==1):
        mn = 'Monday'
   if(dn==2):
        mn='Tuesday'
   if(dn==3):
        mn = 'Wednesday'
   if(dn==4):
        mn = 'Thursday'
   if(dn==5):
        mn = 'Friday'
   if(dn==6):
        mn = 'Saturday'
   if(dn==7):
        mn = 'Sunday'
    
   return mn
    
import time
for i in range(3):
    inpNum=int(input())
    start=time.time()
    print(printDay(inpNum))
    print((time.time()-start)*100000)
    start=time.time()
    print(printDay1(inpNum))
    print((time.time()-start)*100000)



