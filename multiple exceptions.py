try:
    num1,num2=eval(input("Enter two numbers seperated by a comma :"))
    result=num1/num2
    print("result is",result)
    #Using multiple exept block for different type of error

except ZeroDivisionError:
   print("division by 0 is error !!")
except SyntaxError:
    print("comma is missing.enter numbers seperated by comma like this 9,4")
except:
 print("Wrong input")
else:
 print("non except")
finally:
  print("This will no matter what")