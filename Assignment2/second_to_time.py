
Seconds1 = int(input("Enter the seconds : "))
Hours = Seconds1 // 3600
Minutes = (Seconds1% 3600) // 60
Seconds2 = Seconds1 % 60

print(f"Result : ",Hours,"Hours",Minutes,"minutes",Seconds2,"seconds")