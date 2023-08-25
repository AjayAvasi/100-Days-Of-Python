import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()


def set_keys(player):
    screen.onkey(player.up, "Up")
    screen.onkey(player.down, "Down")
    screen.onkey(player.left, "Left")
    screen.onkey(player.right, "Right")


game_running = True
set_keys(snake)
while game_running:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collisions

    if snake.head.distance(food) < 15:
        food.new_location()
        snake.grow()
        scoreboard.add_to_score(1)

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.delete()
        snake = Snake()
        set_keys(snake)

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.delete()
            snake = Snake()
            set_keys(snake)
screen.exitonclick()
