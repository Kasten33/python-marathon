import time
from turtle import Turtle, Screen


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(-i * 20, 0)
            self.snake.append(segment)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.head.forward(20)

    def addsegment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)

    def extend(self):
        self.addsegment(self.snake[-1].position())

    

    # Direction control
    
    def up(self):
        if self.head.heading() != 270:  # Prevent 180 degree turn
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:  # Prevent 180 degree turn
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:  # Prevent 180 degree turn
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:  # Prevent 180 degree turn
            self.head.setheading(0)

