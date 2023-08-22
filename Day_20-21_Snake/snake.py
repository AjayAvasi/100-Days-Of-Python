from turtle import Screen, Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []

        start_x = 0
        start_y = 0
        for i in range(3):
            tile = Turtle()
            tile.shape("square")
            tile.color("white")
            tile.penup()
            tile.goto(x=start_x, y=start_y)
            self.body.append(tile)
            start_x -= 20

        self.head = self.body[0]

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def grow(self):
        tail = Turtle()
        tail.shape("square")
        tail.color("white")
        tail.penup()
        tail.goto(x=self.body[len(self.body) - 1].xcor(), y=self.body[len(self.body) - 1].ycor())
        self.body.append(tail)
