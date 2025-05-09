#class creation 
class myClass:
    #Private variable
    __privateVar=27
    #Private meathod
    def __privMeth(self):
        print("I'm inside myClass")
    #Funtion to print value of the variable 
    def hello(self):
        print("Private variable value:",myClass.__privateVar)   
#Object creation and meathod call
foo=myClass()
foo.hello()
foo.__privMeth 
