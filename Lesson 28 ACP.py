# Define a Dog class
class Dog:
    def __init__(self, breed_name, size):
        self.breed_name = breed_name
        self.size = size

    def show_details(self):
        print(f"Breed: {self.breed_name}, Size: {self.size}")

# Create instances of different dog breeds
dog1 = Dog("Labrador Retriever", "Large")
dog2 = Dog("Pomeranian", "Small")

# Display details
dog1.show_details()
dog2.show_details()
