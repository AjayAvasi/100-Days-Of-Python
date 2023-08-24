import random
from turtle import Turtle

from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_AMOUNT_CARS = 20


class CarManager:

    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = list()
        self.init_cars()

    def new_level(self):
        self.speed += MOVE_INCREMENT

    def init_cars(self):
        for i in range(STARTING_AMOUNT_CARS):
            new_car = Car(random.choice(COLORS))
            rand_x = random.randint(-280, 280)
            rand_y = random.randint(-240, 280)
            new_car.goto(rand_x, rand_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < -330:
                self.cars.remove(car)

    def spawn_cars(self, amount):
        for i in range(random.randint(amount - 2, amount)):
            new_car = Car(random.choice(COLORS))
            rand_y = random.randint(-240, 280)
            new_car.goto(random.randint(300, 320), rand_y)
            self.cars.append(new_car)

    def did_hit(self, player):
        for car in self.cars:
            if (car.xcor() - 10 < player.xcor() < car.xcor() + 10 and car.distance(player) < 25) or (car.xcor() - 10 > player.xcor() > car.xcor() + 10 and car.distance(player) < 50):
                return True
        return False
