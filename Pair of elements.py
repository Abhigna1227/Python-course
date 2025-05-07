#Create a class
class pair_elements:
    def twoSum(self,nums,target):
        lookup={}
        #iterate through tuple
        for i,num in enumerate(nums):
            if target-num in lookup:
                return(lookup[target-num],i)
            lookup[num]=i
            #take input from user
value = int(input("Enter sum from which you want to make this search :"))
print("index1=%d,index2=%d" % pair_elements((10,20,30,40,50,60,70),value)),