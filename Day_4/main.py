import random

ascii_art = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

player = int(input("Enter 1 for Rock, 2 for Paper, and 3 for Scissors: ")) - 1
print(ascii_art[player])
computer = random.randint(0,2)
print("Computer chose:\n\n"+ascii_art[computer])
if computer == player:
	print("It was a tie")
elif player == computer + 1 or player - computer == -2:
	print("You won!")
else:
	print("You lost")
