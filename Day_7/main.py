import random

import hangman_art
import hangman_word_list

print(hangman_art.logo)

num_wrong = 0

chosen_word = random.choice(hangman_word_list.word_list)
solved = ["_"] * len(chosen_word)
wrong_guesses = ""


while "".join(solved) != chosen_word and num_wrong < 6:
    print(hangman_art.stages[6-num_wrong])
    print(" ".join(solved).upper())
    guess = input("Guess a letter: ").lower()
    if guess in solved or guess in wrong_guesses:
        print("You already guessed this letter. Try Again")
    elif len(guess) != 1:
        print("Please guess one letter.")
    elif guess in chosen_word:
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                solved[i] = guess

    else:
        print("Incorrect Guess!")
        num_wrong += 1
        wrong_guesses += guess
if num_wrong < 6:
    print("You won!!")
else:
    print(hangman_art.stages[0])
    print(f"Game Over! The correct word was \"{chosen_word}\"")
