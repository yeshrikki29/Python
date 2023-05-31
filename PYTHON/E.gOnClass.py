class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers=[]
        
    def add_passengers(self,name):
        if not self.OpenSeats():
            return False
        self.passengers.append(name)
        return True
        
        
    def OpenSeats(self):
        return self.capacity - len(self.passengers)
        
        
flight =Flight(4)


people=["yesh","rikki","abx","der","grf"]
for person in people:
    sucess = flight.add_passengers(person)
    if sucess:
        print(f"Added {person} to a flight successfully")
    else:
        print(f"Failed to add {person} to a flight")