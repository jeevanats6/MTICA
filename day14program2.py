class Dog:
    price=400
    def __init__(self,name,color):
        self.color=color
        self.name=name
    def bark(self):
        print("woof")
        print(self.name, "has" ,self.price,
              "price and its color is", self.color)
        
        
if __name__=="__main__":
    pet1=Cat("ginger",4)
    print(pet1.legs)
    print(pet1.color)
    print(pet1)
        
    pet2=Cat("brown",3)
    print(pet2.color)
    print(pet2.legs)
    print(pet2)
      
     
