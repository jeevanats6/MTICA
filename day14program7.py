class A:
    def first_method(self):
        print("Metod of Class A ...")
        
class B:
    def first_method(self):
        print("Method of Class B ...")
        
class C(B,A):
    def third_method(self):
        print("Method of Class C...")
        
if __name__== '__main__':
    ob=C()
    ob.first_method()
    
    ob.third_method()
        
    
