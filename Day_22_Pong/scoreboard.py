from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x_cor):
        super().__init__()
        self.pu()
        self.color("white")
        self.hideturtle()
        self.goto(x=x_cor, y=220)
        self.score = 0
        self.display()

    def display(self):
        self.clear()
        self.write(f"{self.score}", False, "center", ("Minecraftia", 30, "normal"))

    def increment(self):
        self.score += 1
        self.display()
