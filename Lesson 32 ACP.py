# Base class (Car)
class Car:
    def start(self):
        print("Car is starting.")

    def stop(self):
        print("Car is stopping.")

    def drive(self):
        print("Car is driving.")

# Derived class Ferrari
class Ferrari(Car):
    def start(self):
        print("Ferrari is starting with a roar!")

    def stop(self):
        print("Ferrari is stopping with a smooth brake.")

    def drive(self):
        print("Ferrari is driving at high speed.")

# Derived class BMW
class BMW(Car):
    def start(self):
        print("BMW is starting with a powerful engine sound.")

    def stop(self):
        print("BMW is stopping with precise control.")

    def drive(self):
        print("BMW is driving comfortably.")

# Polymorphism in action
def car_test(car):
    car.start()
    car.drive()
    car.stop()

# Create objects for Ferrari and BMW
ferrari = Ferrari()
bmw = BMW()

# Test the polymorphism
print("Testing Ferrari:")
car_test(ferrari)

print("\nTesting BMW:")
car_test(bmw)
