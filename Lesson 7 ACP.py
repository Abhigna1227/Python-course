char = input("Enter an alphabet: ")

# Check if the input is a single character
if len(char) == 1 and char.isalpha():
    ascii_value = ord(char)
    print(f"The ASCII value of '{char}' is {ascii_value}")
else:
    print("Please enter a single alphabet character.")

