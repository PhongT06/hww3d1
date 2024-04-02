#1
class Vehicle():
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
        print(f"Previous Owner: {self.owner}")

    def update_owner(self, new_owner):
            self.owner = new_owner
            print(f"Owner updated: {self.owner}")


vehicle1 = Vehicle("345h3d34gftr32", "Car", "Amy")
vehicle2 = Vehicle("982we43ii2j3v4", "SUV", "Rand")
vehicle3 = Vehicle("897nw849o63bd9", "Truck", "Jill")

vehicle1.update_owner("Jane")
vehicle2.update_owner("Molly")
vehicle3.update_owner("Jack")

print("\nUpdated Owners:")
print(f"The {vehicle1.type} now belongs to {vehicle1.owner}")
print(f"The {vehicle2.type} now belongs to {vehicle2.owner}")
print(f"The {vehicle3.type} now belongs to {vehicle3.owner}")


#2

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0
        
    def add_participant(self):
        self.participant_count += 1
    
    def get_participation_count(self):
        return self.participant_count

event = Event("Code Wars", "04-1-2024")    

event.add_participant()
event.add_participant()
event.add_participant()

print(f"The number of participants for {event.name} is: {event.get_participation_count()}")








