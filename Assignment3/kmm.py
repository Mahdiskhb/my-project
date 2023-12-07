num1 = int(input("enter the first nubmer: "))
num2= int(input("enter the second nubmer: "))
x = num1* num2
for i in range(max(num1, num2), num1 * num2+ 1):
    if i % num1 == 0 and i % num2 == 0:
        x = i
        break
print("the KMM is:", x)