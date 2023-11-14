
import math

print("welcome to calculator")
print("+:sum")
print("-:sub")
print("*:mul")
print("/:div")
print("sqrt")
print("sin")
print("cos")
print("tan")
print("cot")
print("log")
print("factorial")

op = input("enter your choise:")


if op=="+"or op=="-" or op=="*" or op=="/":
    num1=float(input("enter number 1:"))
    num2=float(input("enter number 2:"))
else:
    num3=float(input("enter number"))

if op =="+":
        
        result=num1+num2

elif op=="-":
        
        result= num1-num2

elif op== "*":
        
        result=num1*num2

elif op=="/":

    if num2==0:
            
            result=print("cant divide by 0")
    else:
           result=num1/num2

elif op=="sqrt":
         
         radians=math.radians(num3)
         result=math.sqrt(radians)

elif op=="sin":
       
       radians=math.radians(num3)
       result=math.sin(radians)  

elif op=="cos":
       
       radians=math.radians(num3)
       result=math.cos(radians)

elif op=="tan":
       
       radians=math.radians(num3)
       result=math.tan(radians)

elif op=="cot":
       
       radians=math.radians(num3)
       result=1/math.tan(radians)

elif op=="log":
       
       result=math.log(num3)
       
elif op== "factorial":
       
       result=math.factorial(num3)

print(result)              
       
                                   
        




