from turtle import Turtle, Screen
from Player import Player
from Cars import Car
from ScoreBoard import SBoard1
import time

player = Player((0, -300))
car = Car()
sb = SBoard1()

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

On = True
while On:
    screen.update()
    time.sleep(0.1)
    

screen.exitonclick()