import random
computer_number=random.randint(1,11)
counter=0
while True :
    user_number=int(input("enter a number between 1 to 10 :  "))
    counter+=1
    if computer_number==user_number:
        print ("you win 😎")
        print("the number of your guess is:  "+str(counter))
        break
    elif computer_number>user_number:
        print("bigger than your guess👀")
    elif computer_number<user_number:
        print("smaller than your guess👀")
