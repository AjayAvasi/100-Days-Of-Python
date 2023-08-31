import tkinter.messagebox
from tkinter import *

window = Tk()

window.title("Miles To Kilometers")
window.minsize(width=300, height=75)
window.config(padx=20, pady=20)

# On Event Methods
def on_calculate():
    miles = 0
    try:
        miles = float(miles_entry.get())
    except ValueError:
        tkinter.messagebox.showerror(message="Please enter only numbers", title="Invalid Input")
    kilometers["text"] = str(round(miles * 1.609))


# Window Setup
miles_entry = Entry(width=10)
miles_entry.insert(string="0", index=END)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

kilometers = Label(text="0")
kilometers.grid(column=1, row=1)

kilometers_label = Label(text="Km")
kilometers_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=on_calculate)
calc_button.grid(column=1, row=2)
# Has to be at the end
window.mainloop()
