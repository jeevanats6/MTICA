class circle:
    pi=22/7
    def __init__(self,radius):
        self.radius=radius
        
    def calculateArea(self):
        temp=self.pi*self.radius**2
        return temp
    def calculatePerimeter(self):
        temp=2*self.pi*self.radius
        return temp
        return self.pi*self.radius
r=int(input())
    


ob=circle(r)
area=ob.calculateArea()
peri=ob.calculateperimeter()
print('Area of circle with radius ',r,'is',area)
print('perimeter of circle with radius ',r,'is',peri)
