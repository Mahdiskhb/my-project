
num1=int(input("enter a number : "))
def star(n):
    for i in range (n):
             print(' '*(n-i-1) + '* '*(i+1) )
    for j in range(n):
        print(' '*(j+1) + '* '*(n-j-1))
star(num1)


