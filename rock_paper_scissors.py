"""
100 days of Python course
DAY 4
"""

# the classic game of rock / paper / scissors, where
# rock beats scissors, paper beats rock and scissors beats paper
# using the random module and art supplied - note the three ''' which
# defines it
import random

# pylint identified that rock, paper and scissors should be uppercase
# as they are constants. Ignored for now.
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

# store the images provided above in a list
game_images = [rock, paper, scissors]

# after selection the program will confirm user choice by printing image
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

# the .randint produces either 0 or 1 or 2 (three choices)
computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(game_images[computer_choice])

# using the classic game rules the if / elif process gives outcome
# note there is no else statement as the choices are exhausted
# and the only outcomes are win / lose / draw
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")
