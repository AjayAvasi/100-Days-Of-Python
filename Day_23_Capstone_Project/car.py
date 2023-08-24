from turtle import Turtle


class Car(Turtle):
    def __init__(self, color):
        super().__init__()

        self.pu()
        self.setheading(180)
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(color)
