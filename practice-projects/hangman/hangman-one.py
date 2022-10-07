"""
#Step 1
word_list = ["aardvark", "baboon", "camel"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
"""
#TODO1 - code
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO2 - code
guess = input("Guess a letter\n").lower()
print(guess)

#TODO3 - code
if guess in chosen_word:
    print("Entered letter is part of the word,keep going!")
else:
    print("Entered letter is not part of the word,so will LOSE A LIFE!")