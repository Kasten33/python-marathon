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
        self.move_speed = 20

    def move(self):
        new_x = self.xcor() + self.move_speed
        new_y = self.ycor()
        self.goto(new_x, new_y)

    def levelX(self):
        self.move_speed *= 2
    
    def spawn(self):
        cars = []
        numC = random.randint(75, 100)
        for _ in range(numC):
            car = Car()
            car.goto(random.randint(-650, -300), random.randint(-450, 450))
            car.move_speed *= random.uniform(0.1, 0.6)
            cars.append(car)
            car.move()
        return cars
    
    def clear_cars(self, cars):
        for car in cars:
            car.clear()
            car.hideturtle()
        cars.clear()
