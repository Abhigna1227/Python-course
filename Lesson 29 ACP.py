import math

# Ask the user for the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate area and perimeter (circumference)
area = math.pi * radius * radius
perimeter = 2 * math.pi * radius

# Print the results
print(f"\nFor a circle with radius {radius}:")
print(f"Area = {area:.2f}")
print(f"Perimeter (Circumference) = {perimeter:.2f}")
