
score1=float(input("enter the score 1:"))
score2=float(input("enter the score 2:"))
score3=float(input("enter the score 3:"))
avg=(score1+score2+score3)/3
if avg>=17:
    print("The average is", {avg}, "and that's great.")
elif 17>avg>=12:
    print("The average is ",{avg}," and that's ok.")    
elif  avg<12:
    print("The average is", {avg}," and  you failed ")
