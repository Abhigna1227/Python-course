import random
option=["rock","paper","scissors"]
user_choice = input("Choose rock , paper,or scissors")
computer_choice = random.choice(option)
print("You chose,",user_choice)
print("I chose:",computer_choice)
if user_choice == computer_choice:
    print("no way it is a tie!")
elif user_choice=="rock"and computer_choice=="Scissors":
    print("Rock smashes scissors you win") 
elif user_choice=="paper"and computer_choice=="rock":
 print("paper covers rock so you win")
elif user_choice=="scissors"and computer_choice=="paper":
 print("scissors cuts paper! so you win")
else:
  print("ha! accept defeat you loose")
