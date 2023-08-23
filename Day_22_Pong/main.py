import time
from turtle import Turtle,Screen
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle

screen = Screen()
screen.listen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.tracer(0)

player = Paddle(-350, 0)
computer = Paddle(350, 0)
ball = Ball()
player_score = Scoreboard(-30)
computer_score = Scoreboard(30)

screen.onkeypress(player.go_up, "w")
screen.onkeypress(player.go_down, "s")

game_on = True
computer_going_up = True
# Mark Center
billy = Turtle()
billy.hideturtle()
billy.pu()
billy.goto(0, 300)
billy.color("white")
billy.setheading(270)
billy.pensize(3)
for i in range(30):
    billy.pendown()
    billy.forward(10)
    billy.pu()
    billy.forward(10)

while game_on:
    screen.update()
    time.sleep(0.01)
    # Computer Movement
    if computer_going_up:
        computer.go_up()
    else:
        computer.go_down()

    computer.goto(computer.xcor(), ball.ycor())
    player.goto(player.xcor(), ball.ycor())
    if computer.ycor() > 235 or computer.ycor() < -235:
        computer_going_up = not computer_going_up
    # Ball Movement
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
    if (player.distance(ball) < 50 and ball.xcor() < -330 and 90 < ball.heading() < 270) or (
            computer.distance(ball) < 50 and ball.xcor() > 330 and (ball.heading() > 270 or ball.heading() < 90)):
        ball.hit()

    # Point Scoring
    if ball.xcor() > 390:
        player_score.increment()
        ball.reset_point()
    elif ball.xcor() < -390:
        computer_score.increment()
        ball.reset_point()


screen.exitonclick()
