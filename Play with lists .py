L=[4,5,1,2,9,7,10,8]
print("original List:",L)
#variable to store sum
#The list
count=0
#Finding the sum
for i in L:
    count +=i
#Devide the total elements by
#Number of elements
avg = count/len(L)
print("sum=",count)
print("avrage=",avg)
#Sorting the elements of the lists
L.sort()
#Printing the first elements 
print("Smallest elements is:",L[0])
#Printing the last element
print("Largest element is :",L[-1])
