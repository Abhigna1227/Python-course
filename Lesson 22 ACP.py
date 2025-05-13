# Define the tuple
numbers = (2, 3, 4, 5)

# Start with 1 because it's the identity for multiplication
product = 1

# Loop through the tuple and multiply each number
for num in numbers:
    product *= num

# Print the result
print(f"The product of all values in the tuple is: {product}")
