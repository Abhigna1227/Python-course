num = int(input("Enter a number: "))
odd_numbers = [i for i in range(num) if i % 2 != 0]
another_odd_list = [i for i in odd_numbers]  
print("Odd numbers:", odd_numbers)
print("Another list of odd numbers:", another_odd_list)
