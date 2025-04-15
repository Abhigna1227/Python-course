def add (P,Q):
 #this function is used for adding 2 numbers
 return P+Q
def subtract(P,Q):
 #this function is used for subtracting 2 numbers return P-Q
def multiply(P,Q):
  #This function is used for multiplying 2 numbers P*Q
  return P*Q
def devide(P,Q):
   #This function is used for deviding two numbers 
  return P/Q
   #Now we will take inputs from the user
print("Please select the operaton")
print("a,Add")
print("b,subtract")
print("c,multiply")
print("d,Devide")
choice=input("Please enter choice (a/b/c/d):")
num_1=int(input("Please enter first number:"))
num_2=int(input("Please enter second number:"))
if choice=='a':
    print(num_1 "+",num_2"="add(num_1,num_2))
elif choice == 'b':
      print(num_1 "-",num_2"="subtract(num_1,num_2))
elif choice == 'b':
      print(num_1 "-",num_2"="subtract(num_1,num_2))
elif choice == 'c':
      print(num_1 "*",num_2"="multiply(num_1,num_2))
elif choice == 'd':
      print(num_1 " / ",num_2"="devide(num_1,num_2))

