list1=[1,2,3,4]
list2=[5,6,7,8]
result=map(lambda x,y:x+y,list1,list2)
print("list1+list2")
print(list(result))
def square(n):
    return n**2
list3=[9,0,1,2]
answer=map(square,list3)
print(list(answer))