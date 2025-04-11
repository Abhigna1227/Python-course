#Take input from user
rows=int(input("please enter the total number of rows :"))
number=1 #initialise by 1
print("Floyid's triangle")
#Outer loop for number of rows
for i in range(1,rows+1):
 #inner loops for coloumns
 for j in range(1,i+1):
 #Display results
  print(number, end='')
  number=number+1
 print()