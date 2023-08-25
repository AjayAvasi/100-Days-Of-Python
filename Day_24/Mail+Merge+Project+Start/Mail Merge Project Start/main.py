# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def get_all_names():
    with open("./Input/Names/invited_names.txt") as f:
        names = f.readlines()
    for i in range(len(names)):
        names[i] = names[i].strip()
    return names


def get_template():
    with open("./Input/Letters/starting_letter.txt") as f:
        return f.read()


def create_letter(template, name):
    letter = template.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as f:
        f.write(letter)

template = get_template()
names = get_all_names()

for name in names:
    create_letter(template, name)

