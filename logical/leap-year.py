"""
💪This is a Difficult Challenge 💪
Instructions
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:
This is how you work out whether if a particular year is a leap year.
on every year that is evenly divisible by 4
**except** every year that is evenly divisible by 100
**unless** the year is also evenly divisible by 400
e.g. The year 2000:
2000 ÷ 4 = 500 (Leap)
2000 ÷ 100 = 20 (Not Leap)
2000 ÷ 400 = 5 (Leap!)
So the year 2000 is a leap year.
But the year 2100 is not a leap year because:
2100 ÷ 4 = 525 (Leap)
2100 ÷ 100 = 21 (Not Leap)
2100 ÷ 400 = 5.25 (Not Leap)
"""
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
reminder_four = year % 4
reminder_h = year % 100
reminder_fourh = year % 400
#print(reminder_four)
if reminder_four != 0:
    print("Not leap year")
elif reminder_h != 0:
    print("Leap year")
elif reminder_fourh == 0:
    print("Leap year")
else:
    print("Not leap year")

#reminder_h=year % 100

#print(remainder_four)
#remainder_h=year/100
#remainder_fourh=year/400
#if remainder_four=1:
    #print(Not a leap year)
#if reminder_four=0:
    #check remainder_h=0:
