def printweek(n):
    default= "invalid "
    switcher={
    0:'sun',
    1:'mon',
    2:'tue',
    3:'wed',
    4:'thu',
    5:'fri',
    6:'sat',
    
    }
    return switcher.get(n,'invalid')
for i in range(7):
    inp=int(input())
    print(printweek(inp))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
