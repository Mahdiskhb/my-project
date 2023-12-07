import random
def choose_word():
    word_list=["mango","strawberry","watermelon","persimmon","tangerine","grape","apple","orange","banana","kiwi"]
    return random.choice(word_list)
def HangMan():
    word=choose_word()
    guessed_letters=[]
    attemps=0
    max_attemps=6
    print("welcom to hangman ✋🏻")
    while attemps<max_attemps:
        display_word=""
        for letter in word:
            if letter in guessed_letters:
                display_word+=letter
            else:
                display_word+="_"
        if display_word==word:
            print(f"congratulations🎉 you guessed the word : {word}")   
            break
        print (f"The word : {display_word}")
        print (f"Attemps left : {max_attemps-attemps}")

        guess=input("guess a letter :  ").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("please enter a valid letter")
            continue
        guessed_letters.append(guess)
        if guess not in word:
            attemps+=1
            print(f"sorry,{guess} is not in the word ")
        else:
            print(f"Good guess  {guess} is in the word ")
    if attemps==max_attemps:
        print(f"sorry, you ran out of attemps . the word was:  {word}")
HangMan()                    
