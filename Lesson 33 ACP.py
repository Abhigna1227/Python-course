def int_to_roman(number):
    # Dictionary of roman numerals in descending order
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    roman_num = ""
    i = 0
    
    while number > 0:
        count = number // val[i]
        roman_num += syms[i] * count
        number -= val[i] * count
        i += 1

    return roman_num

# Ask the user for a number
num = int(input("Enter an integer (1 to 3999): "))

# Check if it's in a valid range
if 1 <= num <= 3999:
    print(f"The Roman numeral is: {int_to_roman(num)}")
else:
    print("Oops! Please enter a number between 1 and 3999.")
