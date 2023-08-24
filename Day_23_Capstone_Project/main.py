import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(player.move_up, "Up")

game_is_on = True
counter = 0
while game_is_on:
    car_manager.move_cars()
    if car_manager.did_hit(player):
        scoreboard.game_over()
        game_is_on = False
    time.sleep(0.1)
    screen.update()
    if player.ycor() > FINISH_LINE_Y:
        player.start()
        scoreboard.new_level()
        car_manager.new_level()

    if counter % 20 == 0:
        car_manager.spawn_cars(5)
    counter += 1

screen.exitonclick()
