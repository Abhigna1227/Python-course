b1={6,8,7}
b2={'a','b','h'}
b3=list(zip(b1,b2))
print(b3)
list1=[1,2,3,4]
list2=[8,7,6,5]
for x,y in zip(list1,list2[::-1]):
    print(x,y)