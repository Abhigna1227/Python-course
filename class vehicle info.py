#create class
class vehicles:
 #create init meathod
 def __init__(self,max_speed,mileage):
  #Blind the arguments
  self.max_speed = max_speed
  self.mileage= mileage
#Object creation
modelX = vehicles(240,18)
#access the variable s inside the init meathod
print("Model Max speed:",modelX.max_speed)
print("Model milage:", modelX.mileage)