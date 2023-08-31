from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
TITLE = "Pomodoro Timer"
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    if timer is not None:
        window.after_cancel(timer)
        label_title["text"] = TITLE
        canvas.itemconfig(timer_text, text="00:00")
        check_label["text"] = ""
        global reps
        reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps != 0 and reps % 7 == 0:
        label_title.config(text="Long Break", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        label_title.config(text="Work", fg=GREEN)
        countdown(WORK_MIN * 60)
    else:
        label_title.config(text="Short Break", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(time):
    if time < 0:
        global reps
        reps += 1
        start_timer()
        return
    mins = time // 60
    secs = time % 60
    if secs < 10:
        secs = f"0{secs}"
    if mins < 10:
        mins = f"0{mins}"
    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    global timer
    timer = window.after(1000, countdown, time - 1)

    checkmarks = "✔" * ((reps+1)//2)
    check_label.config(text=checkmarks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

label_title = Label(text=TITLE, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label_title.grid(column=1, row=0)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", width=7, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=7, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()
