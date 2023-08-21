import turtle
from turtle import Turtle, Screen
import random
import colorgram

billy = Turtle()
billy.shape("turtle")
billy.color("red")
turtle.colormode(255)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def square():
    for i in range(4):
        billy.right(90)
        billy.forward(100)


def dash_line():
    for i in range(15):
        billy.forward(10)
        billy.pu()
        billy.forward(10)
        billy.pd()


def diff_shapes():
    for i in range(3, 11):

        billy.pencolor(random_color())
        for j in range(i):
            billy.forward(50)
            billy.right(360 / i)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def random_walk():
    billy.speed("fastest")

    for i in range(200):
        rand_color = random_color()
        billy.pencolor(rand_color)
        billy.fillcolor(rand_color)
        billy.pensize(10)
        billy.setheading(random.randint(0, 3) * 90)
        billy.forward(30)
    billy.speed("normal")


def spirograph(num_of_circles):
    billy.speed("fastest")

    for i in range(num_of_circles):
        billy.pencolor(random_color())
        billy.circle(100)
        billy.right(360 / num_of_circles)


def dot_painting():
    billy.hideturtle()
    extracted_colors = list()
    for color in colorgram.extract("image.jpg", 161):
        extracted_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    del extracted_colors[0]
    billy.penup()

    for i in range(10):
        billy.goto((-250, -300 + i * 50))
        draw_row(extracted_colors)



def draw_row(e_colors):
    for i in range(10):
        billy.pd()
        rand_color = random.choice(e_colors)
        billy.color(rand_color)
        billy.fillcolor(rand_color)
        billy.dot(20)
        billy.pu()
        billy.forward(50)



dot_painting()
screen = turtle.Screen()
screen.exitonclick()
