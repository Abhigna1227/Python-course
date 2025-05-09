age = input("Hi can you please enter your age: ")

if age.isdigit():
    print("Oh thanks, nice knowing your age!")
elif "." in age:
    print("Hey, only non-decimal numbers are allowed.")
else:
    print("This is not a valid age. Please enter a real age.")
