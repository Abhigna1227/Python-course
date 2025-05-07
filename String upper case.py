 #Create class
class IOString():
    #Constructor to get default value
    def __init__(self):
      self.str1=""
        #function to get the input from the user
    def get_String(self):
            self.str1=input("enter string:")
           #Function to print the string inn upper case
    def print_String(self):
            print("The result is ",self.str1.upper())
 #Object creation
string1=IOString()
#Call function
string1.get_String()
string1.print_String()
           
            
