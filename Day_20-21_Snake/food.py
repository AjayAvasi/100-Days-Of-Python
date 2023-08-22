from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.new_location()

    def new_location(self):
        rand_x = random.randint(-14,14) * 20
        rand_y = random.randint(-14,14) * 20
        self.goto(x=rand_x, y=rand_y)