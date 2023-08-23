from turtle import Turtle

SPEED = 3


class Paddle(Turtle):

    def __init__(self, start_x, start_y):
        super().__init__()
        self.pu()
        self.goto(start_x, start_y)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

    def go_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + SPEED)

    def go_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - SPEED)
