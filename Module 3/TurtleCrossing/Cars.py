from turtle import Turtle
import random

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        colors = ["red", "blue", "green", "yellow", "purple", "orange"]
        self.color(random.choice(colors))
        self.penup()
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.x_move = 20
        self.move_speed = 1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor()
        self.goto(new_x, new_y)

    def levelX(self):
        self.move_speed *= 0.8
    
    def spawn(self):
        cars1 = []
        numC = random.randint(5, 15)
        for _ in range(numC):
            car = Car()
            car.goto(random.randint(350, 400), random.randint(-250, 250))
            car.move_speed *= random.uniform(0.1, 0.9)
            cars1.append(car)
        return cars1