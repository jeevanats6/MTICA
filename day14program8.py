class A:
    def first_method(self):
        print("Metod of Class A ...")
        
class B(A):
    def first_method(self):
        print("Method of Class B ...")
        super().first_method()

ob=B()
ob.first_method()
