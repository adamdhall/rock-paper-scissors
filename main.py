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

import random

you_play = input("Welcome to the rock paper scirros game\n rock, paper, or scissors?\n")

computer_choice = ["rock", "paper", "scissors"]
computer_play = computer_choice[random.randint(0, 2)]



if you_play == "rock":
  print(rock)

if you_play == "paper":
  print(paper)

if you_play == "scissors":
  print(scissors)

print("computer plays\n")

if computer_play == "rock":
  print(rock)

if computer_play == "paper":
  print(paper)

if computer_play == "scissors":
  print(scissors)

if you_play == "rock"and computer_play == "rock":
  print("It's a tie!")
elif you_play == "rock" and computer_play == "paper":
    print("you lose!")
elif you_play == "rock" and computer_play == "scissors":
  print("you win!")

elif you_play == "paper" and computer_play == "paper":
    print ("It's a tie!")
elif you_play == "paper" and computer_play == "scissors":
    print("you lose!")
elif you_play == "paper" and computer_play == "rock":
    print("you win!")

elif you_play == "scissors" and computer_play == "scissors":
    print("It's a tie!")
elif you_play == "scissors" and computer_play == "rock":
    print("you lose!")
elif you_play == "scissors" and computer_play == "paper":
    print("you win!")

else:
  print("you picked an invalid input, please try again. ")

