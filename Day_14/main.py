import random
import os
import art
import game_data


def game():
    person_1 = random.choice(game_data.data)
    person_2 = random.choice(game_data.data)

    score = 0

    wrong_answer = False
    while not wrong_answer:
        display_comparison(person_1, person_2, score)
        guess = input("Who do you think has more followers? Type '1' or '2': ")
        if (guess == "1" and person_1["follower_count"] >= person_2["follower_count"]) or (
                guess == "2" and person_1["follower_count"] <= person_2["follower_count"]):
            score += 1
            person_1 = person_2
            person_2 = random.choice(game_data.data)
            display_comparison(person_1, person_2, score)
        else:
            end_screen(score)
            wrong_answer = True


def display_comparison(person_1, person_2, score):
    os.system("cls")
    print(art.logo)

    if score != 0:
        print(f"That's correct! Your current score is {score}!")
    print(f"Account 1: {person_1['name']}, a {person_1['description']} from {person_1['country']}")
    print(art.vs)
    print(f"Account 2: {person_2['name']}, a {person_2['description']} from {person_2['country']}")


def end_screen(score):
    os.system("cls")
    print(art.logo)
    print(f"That is wrong! Your final score was {score}")


game()
