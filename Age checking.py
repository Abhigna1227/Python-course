print("Hello, welcome to the class of Raj")

age_str = input("Please enter your age: ")

age = int(age_str)

if age < 10:
    print("Hmm... you are very young, but since you are smart, you will have to take a test. Alright?")
elif age <= 15:
    print("Hmm... you are on the right path. You are allowed to be in my class.")
elif age <= 20:
    print("Uhh... you are a bit late, but fine, you are allowed.")
else:
    print("You are very old. You should be working by now. I am so sorry, but you are not allowed in my class forever.")
