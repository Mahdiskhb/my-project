import random

computer_score=0
player_score=0
computer_choice=""

while computer_score < 5 and player_score < 5:
    guess=random.randint(1,3)
    if guess == 1:

        computer_choice="Rock"

    elif guess == 2:

        computer_choice == "Paper"

    elif guess == 3:

        computer_choice =="Scissor"


    
    player_choice=input("Enter your choice from [Rock - Paper - scissor] : ")

    print("👤 :",player_choice)
    print(" 💻 :",computer_choice)

    if computer_choice == "Rock" and player_choice == "Paper":
        player_score+= 1
    elif computer_choice == "Rock" and player_choice == "Scissor":
        computer_score += 1
    elif computer_choice == "Paper" and player_choice == "Rock":
        computer_score += 1
    elif computer_choice == "Paper" and player_choice == "Scissor":
        player_score += 1 
    elif computer_choice == "Scissor" and player_choice== "Rock":
        player_score += 1
    elif computer_choice == "Scissor" and player_choice == "Paper":
        computer_score +=1
    elif computer_choice == player_choice :
        print("equal")



    print("computer:",computer_score)
    print("user: ",player_score)