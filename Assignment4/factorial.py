number=int(input("please enter the number : "))
num=1
factorial=1
while factorial<number:
    num+=1
    factorial*=num
if factorial==number:
    print("yes✅")
else:
    print("no❌")    

