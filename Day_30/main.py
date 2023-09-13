import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# -----------------------------------SEARCH-------------------------------------- #

def find_password():
    try:
        with open("passwords.json", "r") as f:
            website_name = website_e.get()
            data = json.load(f)[website_name]
            message = f"{website_name}'s Login Info:\n\nEmail: {data['email']}\nPassword: {data['password']}"
    except FileNotFoundError:
        message = "Data File Missing. Try to add some passwords first"
    except KeyError:
        message = "This website does not have any passwords saved."

    messagebox.showinfo(title="Alert!", message=message)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_chars = password_letters + password_numbers + password_symbols

    random.shuffle(password_chars)
    password = "".join(password_chars)
    pyperclip.copy(password)
    return password


def set_password():
    password_e.delete(0, END)
    password_e.insert(0, create_password())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_e.get()
    email = email_e.get()
    password = password_e.get()

    if email == "" or website == "" or password == "":
        messagebox.showerror(title="Invalid Fields", message="Please make sure you have filled out every field")
        return

    # confirmed = messagebox.askokcancel(title="Are you sure?",
    #                                    message=f"Entered Values: \nEmail: {email}\nPassword: {password}\nWebsite: {website}\nDo you want to save?")
    # if not confirmed:
    #     return

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    try:
        with open("passwords.json", "r") as f:
            pass
    except FileNotFoundError:
        with open("passwords.json", "w") as f:
            json.dump(dict(), f, indent=4)
    finally:
        with open("passwords.json", "r") as f:
            data = json.load(f)
            data.update(new_data)
        with open("passwords.json", "w") as f:
            json.dump(data, f, indent=4)

            website_e.delete(0, END)
            password_e.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_l = Label(text="Website:")
website_l.grid(column=0, row=1)

email_l = Label(text="Email/Username:")
email_l.grid(column=0, row=2)

password_l = Label(text="Password:")
password_l.grid(column=0, row=3)

website_e = Entry(width=33)
website_e.focus()
website_e.grid(column=1, row=1)

email_e = Entry(width=42)
email_e.insert(0, "someemail@test.com")
email_e.grid(column=1, row=2, columnspan=2)

password_e = Entry(width=33)
password_e.grid(column=1, row=3)

generate_b = Button(text="Generate", command=set_password)
generate_b.grid(column=2, row=3)

search_b = Button(text="Search", command=find_password)
search_b.grid(column=2, row=1)

add_b = Button(text="Add", width=36, command=save)
add_b.grid(column=1, row=4, columnspan=2)
window.mainloop()
