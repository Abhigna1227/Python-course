import math  # Import the math module to get the value of pi

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius  # Formula for circumference
    return circumference

# Get radius from user
radius = float(input("Enter the radius of the circle: "))

# Call the function and display the result
circumference = calculate_circumference(radius)
print(f"The circumference of the circle with radius {radius} is: {circumference:.2f}")

