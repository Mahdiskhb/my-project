list=[]
num=int(input("enter the length of list  : "))

for i in range(num):
    list.append(input("enter the numbers : "))
    i+1
print(" the list is : ",list)

listm = []
for x in list:
    if x not in listm:
        listm.append(x) 

print("the list is : ",listm)