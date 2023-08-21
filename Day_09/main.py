import art
import os

print(art.logo)
print("Welcome to the secret auction program.")

more_people = True
bids = {}

while more_people:
	name = input("What is your name?: ")
	amt = float(input("What is your bid?: ").replace("$", ""))
	bids[name] = amt
	if input("Are there any other bidders? Type 'yes' or  'no'. ") != "yes":
		more_people = False
	os.system('cls')

highest_bidder = ""

for key in bids:
	if highest_bidder == "":
		highest_bidder = key
	else:
		if bids[key] > bids[highest_bidder]:
			highest_bidder = key

print(f"The highest bidder was {highest_bidder} with the amount ${bids[highest_bidder]}!")
	