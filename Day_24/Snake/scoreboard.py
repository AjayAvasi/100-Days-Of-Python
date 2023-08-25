from turtle import Turtle


def get_high_score():
    with open("high_score.txt", "r") as f:
        return f.read()


def set_high_score(score):
    with open("high_score.txt", "w") as f:
        f.write(str(score))


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.high_score = int(get_high_score())
        self.color("white")
        self.pu()
        self.goto(0, 250)
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center",
                   font=('Courier New', 20, 'bold'))

    def add_to_score(self, points):
        self.score += points
        self.display()

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            set_high_score(self.high_score)
        self.score = 0
        self.display()
