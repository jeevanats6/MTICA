num1=input("enter a number:")
num2=input("enter a number:")

try:
    
    res=int(num1)/int(num2)
except (ZeroDivisionError,ValueError):
    print("Exception handling div by zero")
##except ValueError:
##    print("Exception handling by rev")    
except Exception as ob:
    print(ob)
else:
    print (num1, '/',num2, '=',res)
finally:
    print("thanks")
    
print("visit again at py class at MTICA")
