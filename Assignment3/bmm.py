num1 = int(input("enter the first nubmer: "))
num2 = int(input("enter the second nubmer: "))
x = 1
for i in range(1, min(num1, num2) + 1):
    if num1 * num2 % i == 0:
        x = i
print("the BMM is:", x)
