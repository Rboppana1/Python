#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12

#Welcome to the tip calculator
#What was the total bill?
#What percentage tip would you like to give? 10, 12, or 15?
#How many people to split the bill?
#Each person should pay:

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill?"))
percent_bill = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
percent = percent_bill/100
percent_one = percent+1
print(percent_one)
count = int(input("How many people to split the bill?"))
final = (total_bill / count)*percent_one
final_amount=round(final,2)
print(final)
print(final_amount)
print(input(f"Each person should pay: {final_amount}"))
