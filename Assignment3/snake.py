import random 
a=[]
b=[]
num=int(input("enter the length of snake tail🐍 :"))
for i in range(num):
   a.append(i+1)
   if i %2 ==0:
      b.append("🟢")
   else:
      b.append("🟡")   
print(b)      
     