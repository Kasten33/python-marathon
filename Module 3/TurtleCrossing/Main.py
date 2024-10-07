from turtle import Screen
from Player import Player
from Cars import Car
from ScoreBoard import SBoard1
import time

player = Player((0, -450))
car = Car()
car.hideturtle()
sb = SBoard1()
cars = []

screen = Screen()
   
screen.setup(width=1200, height=1200)
screen.title("Cross the Road")
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")
screen.onkeypress(player.l, "Left")
screen.onkeypress(player.r, "Right")

#game loop

On = True
while On:
    screen.update()
    time.sleep(0.1)

    if player.ycor() > 450:
        player.goto(0, -450)
        sb.increase_level()
        car.clear_cars(cars)  
        cars = car.spawn() 
        for car in cars:
            car.levelX()  

    for car in cars:
        car.move()
        if car.xcor() > 700:
            car.goto(-700, car.ycor())
        if player.distance(car) < 20:  
            On = False
            sb.gameO()

    if player.xcor() > 625:
        sb.gameO()
    if player.xcor() < -625:
        sb.gameO()
        

        
        

screen.exitonclick()