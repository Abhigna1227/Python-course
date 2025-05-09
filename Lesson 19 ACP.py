import math

# Ask the user to enter an angle in degrees
angle_deg = float(input("Enter an angle in degrees: "))

# Convert the angle to radians
angle_rad = math.radians(angle_deg)

# Calculate trigonometric values
sine = math.sin(angle_rad)
cosine = math.cos(angle_rad)
tangent = math.tan(angle_rad)

# Display the results
print(f"Sine({angle_deg}°) = {sine}")
print(f"Cosine({angle_deg}°) = {cosine}")
print(f"Tangent({angle_deg}°) = {tangent}")
