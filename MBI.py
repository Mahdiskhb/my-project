


height=float(input("please enter your height :"))
print("-------------------------------------------------------------")
weight=float(input("please enter your weight :"))

bmi= weight / height ** 2
if bmi < 18.5 :
    print("Underweight")
elif 18.5 <= bmi<= 24.9 :
    print("Normal Weight")
elif 25 <= bmi <= 29.9 :
    print("Overweight")
elif 30 <=bmi <= 34.9 :
    print("Obesity")
elif 35 <= bmi <= 39.9 :
    print("Extreme Obesity")
