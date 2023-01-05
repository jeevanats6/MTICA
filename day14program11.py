class Complex:
     def __init__(self,real,img):
         self.real=real
         self.img=img
     def __add__(self,ob):
         temp=self.real-ob.real,ob.real-ob.img
         return temp
     def __str__(self):
         return (self.real,self.img)
ob1=Complex(6,8)
ob2=Complex(8,5)
ob3=ob1-ob2
##ob4=ob1+ob2
##print(ob3.real)
##print(ob4.img)
print(ob3)
