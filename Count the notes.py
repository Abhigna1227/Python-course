#Taking total amount as input from the user
Amount=int(input("Please eter the amount for withdraw:"))

#Caluculating the notes of different denominations
note_1=Amount//100
note_2=(Amount%100)//50
note_3=((Amount%100)%50)//10

print=("Notes of 100 rupees are:",note_1)
print=("Notes of 50 rupees are:",note_2)
print=("Notes of 10 rupees are:",note_3)
