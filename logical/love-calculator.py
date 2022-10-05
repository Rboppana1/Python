"""
💪 This is a Difficult Challenge 💪
Instructions
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5
L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3
Love Score = 53
Print: "Your score is 53."
"""
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bothnames = name1+name2
#print(bothnames)
true = bothnames.lower().count('t')+bothnames.lower().count('r')+bothnames.lower().count('u')+bothnames.lower().count('e')
#true2 = name2.lower().count('t')+name2.lower().count('r')+name2.lower().count('u')+name1.lower().count('e')
#print(true1)
#print(true2)
#true = true1+true2
#print(true)
love = bothnames.lower().count('l')+bothnames.lower().count('o')+bothnames.lower().count('v')+bothnames.lower().count('e')
#love2 = name2.lower().count('l')+name2.lower().count('o')+name2.lower().count('v')+name1.lower().count('e')
#print(love1)
#print(love2)
#love = love1+love2
#print(love)
truelove = str(true)+str(love)
#print(truelove)
truelove_final= int(truelove)

if (truelove_final < 10) or (truelove_final > 90):
    print(f"Your score is {truelove_final}, you go together like coke and mentos.")
elif (truelove_final > 40) and (truelove_final < 50):
    print(f"Your score is {truelove_final}, you are alright together.")
else:
    print(f"Your score is {truelove_final}")
