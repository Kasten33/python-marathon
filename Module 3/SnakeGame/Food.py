from turtle import Turtle
import random

class Food(Turtle):
        def __init__(self, snake_segments):
            super().__init__()
            self.shape("circle")
            self.penup()
            self.shapesize(stretch_wid=0.5, stretch_len=0.5)
            self.color("blue")
            self.speed("fastest")
            self.refresh(snake_segments)

        def refresh(self, snake_segments):
            while True:
                random_x = random.randint(-280, 280)
                random_y = random.randint(-280, 280)
                if not any(segment.distance(random_x, random_y) < 20 for segment in snake_segments):
                    self.goto(random_x, random_y)
                    break
           