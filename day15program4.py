class vehicle:
    def __init__(self,name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def seating_capacity(self, capacity):
        return f"The seating capacity of a (self.name)\ 50 is (capacity) passengers"
    

class Bus(vehicle):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity = 50)
    
school_bus = Bus("schools Volvo", 180, 12)
print(school_bus.seating_capacity())
                 
