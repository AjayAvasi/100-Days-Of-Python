import random
import turtle
from turtle import Turtle, Screen



screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you think is going to win? Pick a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "grey"]

x = -230

y = -30 * (len(colors)/2)
racers = []
for color in colors:
    turt = Turtle(shape="turtle")
    turt.color(color)
    turt.pu()
    turt.goto(x=x, y=y)
    y += 30
    racers.append(turt)

race_is_on = False
if user_bet:
    race_is_on = True

while race_is_on:
    for racer in racers:
        racer.forward(random.randint(0, 10))
        if racer.xcor() >= 230:
            race_is_on = False
            winner = racer.fillcolor()
            break
if winner == user_bet:
    print(f"You bet correctly! The {winner} turtle won!")
else:
    print(f"You betted on {user_bet}... You guessed incorrectly :( The {winner} turtle won!")
screen.listen()
screen.exitonclick()







def etch_a_sketch():
    billy = Turtle()
    def move_forwards():
        billy.forward(10)

    def move_backwards():
        billy.forward(-10)

    def turn_cw():
        billy.right(10)

    def turn_ccw():
        billy.left(10)

    screen.onkey(fun=move_forwards, key="w")
    screen.onkey(fun=move_backwards, key="s")
    screen.onkey(fun=turn_cw, key="d")
    screen.onkey(fun=turn_ccw, key="a")
    screen.onkey(fun=turtle.resetscreen, key="c")
