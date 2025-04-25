#Create a tuple wiyh different data types 
tuplex=("Tuple",False,3.2,1)
print(tuplex)
#Create a tuple
tuplex = (4,6,2,8,3,1)
print(tuplex)
#tuples are immutable, so you cannot add new elements
#Using merge of tuples with the +Operator you can add an element and it will create a new tuple 
tuplex= tuplex + (9,)
print(tuplex)
#Counts the number of occourances of item 50 from a tuple
tuple1=(50,60,70,50)
print(tuple1.count(50))
#create a tuple 
tuplex = (2,4,3,5,6,7,8,6,1)
#Used tuple[start:stop] thw start index is inclusive and the stop index
_slice = tuplex[3:5]
#is exclusive
print(_slice)
#If the start index isn't defined,is taken from the beginning if the tuple
_slice=tuplex[:6]
print(_slice)