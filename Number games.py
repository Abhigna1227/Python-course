import random #Importing module 
playing=True #initialise
number = str(random.randint(10,20)) #random built in function
print("I will generate a number from 1-20 and you have to guess the number one digit at a time")
print("The game ends you will get 1 hero!")
#Literate loop till the condition is true
while playing:
 guess = input("gimme your best guess!\n")
 if number == guess:
  print("you win the game!")
  print("The number was ",number)
  break 
 else:
  print("Your guess isnt quite right ,try again.\n")