import random
n=[]
number=int(input("enter number between 1 to 100"))
for i in range(number):
    num=random.randint(1,100)
    n.append(num)
    print(n)
    