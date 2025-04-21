 #Using a try and exept
try:
 number = int(input("Enter a number :"))
 print("The number entered is",number)
#using value error 
except ValueError as ex:
 print("exception: ",ex)