listn=[]
for i in range(10):
    x= int(input("enter the number: "))
    listn.append(x)
if listn==sorted(listn):
    print("the array is sorted")
elif listn != sorted(listn):
    print("the array is not sorted")       

print(listn)
