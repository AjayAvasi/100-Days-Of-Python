import art
import random

print(art.logo)

lives = 10

if input("Enter 'easy' or 'hard' mode: ").lower() == 'hard':
    lives = 5

print("Im thinking of a number between 1-100")

answer = random.randint(1, 100)

game_over = False
while not game_over:
    guess = int(input("Pick a number: "))
    if guess > answer:
        lives -= 1
        print(f"My number is lower. You have {lives} guesses left!")

    elif guess < answer:
        lives -= 1
        print(f"My number is higher. You have {lives} guesses left!")

    else:
        print(f"You won! My number was {answer}!")
        game_over = True

    if lives == 0:
        print(f"You lost :( My number was {answer}")
