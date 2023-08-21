import random
import time
import os

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

players_hand = []
dealers_hand = []


def reset():
    os.system("cls")
    print(art.logo)
    players_hand.clear()
    dealers_hand.clear()
    players_hand.append(random.choice(cards))
    players_hand.append(random.choice(cards))
    dealers_hand.append(random.choice(cards))
    dealers_hand.append(random.choice(cards))


def player_hit():
    players_hand.append(random.choice(cards))


def dealer_hit():
    dealers_hand.append(random.choice(cards))


def display_player_score():
    print("Your hand: " + str(players_hand) + ", current score: " + str(sum(players_hand)))


def display_dealer_score():
    print("Dealer hand: " + str(dealers_hand) + ", current score: " + str(sum(dealers_hand)))


def dealer_plays():
    while sum(dealers_hand) <= 16:
        display_dealer_score()
        print("Dealer draws card...")
        time.sleep(3)
        dealer_hit()


def blackjack():
    reset()
    end_game = False

    # Checking both hands prior to input
    if sum(dealers_hand) == 21:
        print("You lost! The dealer got 21!")
        end_game = True
    elif sum(players_hand) == 21:
        print("You won! You got 21!")
        end_game = True
    elif sum(players_hand) > 21:
        if 11 in players_hand:
            players_hand.remove(11)
            players_hand.append(1)
        else:
            print("Bust! You went over 21!")
            end_game = True
    # --------------------------------------
    display_player_score()
    if end_game:
        display_dealer_score()

    while not end_game:

        print("Dealer's first card: " + str(dealers_hand[0]))

        if input("Do you want to hit? 'y'/'n': ") == "y":
            print("\n")
            player_hit()
            display_player_score()
            if sum(players_hand) > 21:
                if 11 in players_hand:
                    players_hand.remove(11)
                    players_hand.append(1)
                else:
                    print("Bust! You went over 21!")
                    end_game = True
            elif sum(players_hand) == 21:
                print("You won! You got 21!")
                end_game = True

        else:
            print("\n")
            dealer_plays()
            display_dealer_score()

            if sum(dealers_hand) > 21:
                if 11 not in dealers_hand:
                    print("Dealer bust! You won!")
                else:
                    dealers_hand.remove(11)
                    dealers_hand.append(1)
                    dealer_plays()
            elif sum(dealers_hand) > sum(players_hand):
                print("You lost! The Dealer got closer to 21!")
            elif sum(dealers_hand) == sum(players_hand):
                print("It's a draw! Both the dealer and the player got the same score!")
            else:
                print("You won! You got a higher score than the dealer!")
            end_game = True
    print("\n-----\nFinal Scores:\n")
    display_player_score()
    display_dealer_score()
    print()


while input("Do you want to play Blackjack? 'y'/'n': ") == 'y':
    blackjack()
