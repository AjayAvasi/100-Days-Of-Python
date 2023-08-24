from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.goto(-210, 250)
        self.level = 1
        self.display()

    def display(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)

    def new_level(self):
        self.level += 1
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", False, "center", FONT)
