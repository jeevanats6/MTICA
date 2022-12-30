def printmonth(n):
    
    if n==1:
        return 'jan'
    if n==2:
        return 'feb'
    if n==3:
        return 'mar '
    if n==4:
        return 'apr '
    if n==5:
        return 'may'
    if n==6:
        return 'jun '
    if n==7:
        return 'jul '
    if n==8:
        return 'aug '
    if n==9:
        return 'sep '
    if n==10:
        return 'oct '
    if n==11:
        return 'nov '
    if n==12:
        return 'dec '
    else:
        return 'invalid input'
def printmonth1(n):
    
    if n==1:
        return 'jan'
    elif n==2:
        return 'feb'
    elif n==3:
        return 'mar '
    elif n==4:
        return 'apr '
    elif n==5:
        return 'may'
    elif n==6:
        return 'jun '
    elif n==7:
        return 'jul '
    elif n==8:
        return 'aug '
    elif n==9:
        return 'sep '
    elif n==10:
        return 'oct '
    elif n==11:
        return 'nov '
    elif n==12:
        return 'dec '
    else:
        return 'invalid input'
    

import time
for i in range(3):
    inpnum=int(input())
    start=time.time()
    print(printmonth(inpnum))
    print(time.time()-start)
    start=time.time()
    print(printmonth1(inpnum))
    print(time.time()-start)



