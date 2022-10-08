# TODO1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
# letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
number = len(chosen_word)
print(number)
display = number * ["_"]
print(display)

# guess = input("Guess a letter\n").lower()
# print(guess)
"""
replace()
print(display)
print(display.count("_"))
"""

def replace():
    for position in range(number):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


i = display.count("_")
while i > 0:
    guess = input("Guess a letter\n").lower()
    replace()
    print(display)
    i = (display.count("_"))
    print(i)

if i == 0:
    print("YOU WON!")

# if guess in chosen_word:
#   print("Entered letter is part of the word,keep going!")
# else:
#    print("Entered letter is not part of the word,so hangman will LOSE A LIFE!")
