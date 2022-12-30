def printmonth(n):
    
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
    
    
for i in range(13):
    inpnum=int(input())
    print(printmonth(inpnum))
