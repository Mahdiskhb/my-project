counter=0
sum=0
while True:
    score=input("Enter score or if you want to exit please enter (exit) ")

    if score == "exit":
        break
    else:
        score = float(score)
        counter+=1
        sum+=score

print(" the Average is : ",sum/counter)