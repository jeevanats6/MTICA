def checkEven(num1):
    
    if num1%2==0:
        return "even"
    return None
def checkOdd(num1):
    if num1%2==1:
        return "odd"
    return None
num=int(input("enter a number"))    
print(checkEven(num))
print(checkOdd(num))


