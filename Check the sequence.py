#Initialise dictionary
test_dict={'Codingal' : 2, 'is' :2, 'best':2, 'for':2, 'Coding':1}
#Printing original dictionary
print("The original dictionary:"+ str(test_dict))
#Inisialise value
K=2
#Using loop
#Selective key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key] ==K:
        res =res+1
#Printing result
print("Frequency of k is:"+str(res))
