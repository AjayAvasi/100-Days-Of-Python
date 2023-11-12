import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Learn A Language")
window.minsize(width=900, height=720)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
title = "French"
word = "Word"


def get_rand_word():
    data = pd.read_csv("./data/french_words.csv")
    random_word = random.choice(data.to_dict(orient="records"))

    return random_word


event = None


def change_word():
    global event
    if event is not None:
        window.after_cancel(event)
    word_pair = get_rand_word()
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=word_pair["French"])

    event = window.after(3000, flip, word_pair["English"])


def flip(word):
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=word)
    global event
    event = None


def correct():
    change_word()


def incorrect():
    change_word()


# -------------------------------UI SETUP-------------------------------------------------------------------------------
card_front = PhotoImage(file="C:\\Users\\Arun\\GithubRepos\\100-Days-Of-Python\\Day_31\\images\\card_front.png")
card_back = PhotoImage(file="C:\\Users\\Arun\\GithubRepos\\100-Days-Of-Python\\Day_31\\images\\card_back.png")

canvas = Canvas(width=800, height=546, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)

card = canvas.create_image(400, 270, image=card_front)

card_title = canvas.create_text(400, 150, text=title, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text=word, font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="C:\\Users\\Arun\\GithubRepos\\100-Days-Of-Python\\Day_31\\images\\wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=incorrect)
wrong_button.grid(row=1, column=0)

right = PhotoImage(file="C:\\Users\\Arun\\GithubRepos\\100-Days-Of-Python\\Day_31\\images\\right.png")
right_button = Button(image=right, highlightthickness=0, command=correct)
right_button.grid(row=1, column=1)

window.mainloop()

# ----------------------------------------------------------------------------------------------------------------------
