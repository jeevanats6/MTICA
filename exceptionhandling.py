##num1=int(input("enter a number:"))
##num2=int(input("enter a number:"))
##
##try:
##    res=num1/num2
##except ZeroDivisionError:
##    print("division by zero not allowed")
##else:
##    print (num1, '/',num2, '=',res)
##print('thanks')


num1=input("enter a number:")
num2=input("enter a number:")

try:
    
    res=int(num1)/int(num2)
except ZeroDivisionError:
    print("Exception handling by dev")
except ValueError:
    print("Exception handling by rev")    
except Exception as ob:
    print(ob)
else:
    print (num1, '/',num2, '=',res)
finally:
    print("thanks")
    
print("visit again at py class at MTICA")
