"""
Instructions
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.
Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
Example Input
56
Example Output
You have 12410 days, 1768 weeks, and 408 months left.
"""
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

remaining_years = 90-int(age)
#print(type(remaining_years))
days=remaining_years*365
weeks=remaining_years*52
months=remaining_years*12
print(f"You have {days} days, {weeks} weeks, and {months} months left")
#You have 9125 days, 1300 weeks, and 300 months left


