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


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_running = True
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
        game_running = False
        scoreboard.game_over()

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_running = False
            scoreboard.game_over()
screen.exitonclick()
