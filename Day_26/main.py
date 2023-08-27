
import pandas

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphabet = {row[1]["letter"]: row[1]["code"] for row in data.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter a name to convert into the Nato Phonetic Alphabet? ")
name = name.upper()
converted = [phonetic_alphabet[letter] for letter in name]
print(converted)
