# Ask the user to enter a number (can be multiple digits)
user_input = input("Enter a number: ")

# Initialize a counter
digit_count = 0

# Loop through each character in the input
for char in user_input:
    if char.isdigit():  # Check if the character is a digit
        digit_count += 1

# Print the result
print("You entered", digit_count, "digit(s).")
