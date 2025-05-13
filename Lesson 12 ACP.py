def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    
    binary_number = ""
    
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2
    
    return binary_number

# Take integer input from the user
try:
    decimal_number = int(input("Enter a decimal number: "))
    binary_number = decimal_to_binary(decimal_number)
    print(f"The binary equivalent of {decimal_number} is {binary_number}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
