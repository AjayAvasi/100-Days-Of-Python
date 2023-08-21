import art


print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
want_to_continue = True

while want_to_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def cesar(text, shift, direction):
        if direction != "decode" and direction != "encode":
            print("Wrong input. Only choose between 'encode' and 'decode'")
        else:
            if direction == "decode":
                shift *= -1
            converted = ""
            for letter in text:
                if letter not in alphabet:
                    converted += letter
                    continue
                position = alphabet.index(letter)
                converted += alphabet[(position + shift)%26]
            print(f"The {direction}d text is \"{converted}\"")

    cesar(text, shift, direction)
    want_to_continue = input("Type 'yes' if you want to restart the cipher program. Otherwise type 'no'.\n") == "yes"

print("Goodbye")