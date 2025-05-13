# Ask the user how many rows
rows = int(input("How many rows for the triangle? "))

# Loop to print the triangle
for i in range(1, rows + 1):
    # Print spaces first (to push stars to the right!)
    print(" " * (rows - i) + "*" * i)
