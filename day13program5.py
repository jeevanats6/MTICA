def squres(x=0):
    while x<10:
        x = x+1
        yield x*x
        
yieldedList=[i for i in squres()]
print(yieldedList)
