import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")
        self.setheading(180)
        self.speed = 6

    def move(self):
        self.forward(self.speed)

    def bounce(self):
        self.setheading(-self.heading())

    def hit(self):
        if self.heading() > 270 or self.heading() < 90:
            self.setheading(random.randint(135, 225))
        else:
            self.setheading(random.randint(-45, 45))
        self.speed += 0.5

    def reset_point(self):
        self.goto(0, 0)
        self.hit()
        self.speed = 6
