# Parent class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage  # in km per liter (just for fun)
        self.capacity = capacity  # how many people can sit

    def show_info(self):
        print(f"Vehicle Name: {self.name}")
        print(f"Mileage: {self.mileage} km/l")
        print(f"Capacity: {self.capacity} passengers")

# Child class (Bus)
class Bus(Vehicle):
    def calculate_fare(self):
        # Let's say the fare is ₹100 per person
        fare_per_person = 100
        total_fare = self.capacity * fare_per_person
        return total_fare

# Let's create a Bus object!
my_bus = Bus("City Express", 6, 50)

# Showing info
my_bus.show_info()

# Calculating total fare
total = my_bus.calculate_fare()
print(f"Total Bus Fare for all passengers: ${total}")
