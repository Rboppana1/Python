"""
Instructions
Make a rock, paper, scissors game.
Start the game by asking the player:
"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
From there you will need to figure out:
How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.
You can find the "official" rules of the game on the World Rock Paper Scissors Association website.

"""
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]
player_choose=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
player_choice=int(player_choose)
#print(player_choice)
print(game_images[player_choice])

computer_choice= random.randint(0,2)
print(f"computer choice: {computer_choice}")
print(game_images[computer_choice])

if player_choice == computer_choice:
    print("Its a draw")
#Paper(1) beats Rock(0),Scissors(2) beats Paper(1),Rock(0) beats Scissors(2)
elif player_choice == 2 and computer_choice == 0:
    print("Computer Won!")
elif computer_choice == 2 and player_choice == 0:
    print("You Won!")
elif computer_choice > player_choice:
    print("Computer Won!")
else:
    print("You Won!")


