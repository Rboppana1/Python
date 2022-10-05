"""""
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
"""
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_final=round(weight/height ** 2)
#bmi_final=round(bmi,0)
#print(bmi_final)

if bmi_final <= 18.5:
    print(f"Your BMI is {bmi_final}, you are underweight.")
elif bmi_final <= 25:
    print(f"Your BMI is {bmi_final}, you have a normal weight.")
elif bmi_final <= 30:
    print(f"Your BMI is {bmi_final}, you are slightly overweight.")
elif bmi_final <= 35:
    print(f"Your BMI is {bmi_final}, you are obese.")
else:
    print(f"Your BMI is {bmi_final}, you are clinically obese.")