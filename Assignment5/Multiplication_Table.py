num1=int(input("enter the number 1: "))
num2=int(input("enter the number 2: "))
table =[[i*j for j in range(num1,num2) ] for i in range (num1,num2)]  
for row in table:
    for item in row:
        print(item,end='\t')
    print()