def checkEvenOdd(num1):
    assert(num1>0),"-ve numbers"
    if num1%2==0:
        return "even"
    else:
        return "0dd"

for i in range(3):    
    num=int(input("enter a number"))
    try:        
        print(num,"is",checkEvenOdd(num))
    except AssertionError as ob:
        print(ob)
