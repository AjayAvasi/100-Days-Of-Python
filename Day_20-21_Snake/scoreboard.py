from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(0, 250)
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Courier New', 20, 'bold'))

    def add_to_score(self, points):
        self.score += points
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Courier New', 25, 'bold'))
