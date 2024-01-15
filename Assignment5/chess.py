num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
def chess(num1,num2):
    for i in range(num1):
        if i%2==0:
            for k in range(num2):
                if k%2==0:
                    print("⬛",end="")
                else:
                    print("⬜",end="")
            print("")
        else:
            for k in range(num2):
                if k%2==0:
                    print("⬜",end="")
                else:
                    print("⬛",end="")
            print("")
chess(num1,num2)                                        