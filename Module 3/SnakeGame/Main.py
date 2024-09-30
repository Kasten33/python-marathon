from turtle import Screen
from Food import Food
from Snake import Snake
from ScoreBoard import SBoard
import time

# Screen setup

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # Turn off screen updates
snake = Snake() # Spawns the snake
food = Food(snake.snake) # Spawns the food
scoreboard = SBoard() # Spawns the scoreboard

# Key bindings

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


On = True

# Main game loop

while On:
    screen.update()
    time.sleep(0.1) 
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh(snake.snake)
        snake.extend()
        scoreboard.update_score()

    if snake.head.xcor() > 290:
        snake.head.setx(-290)
    elif snake.head.xcor() < -290:
        snake.head.setx(290)
    elif snake.head.ycor() > 290:
        snake.head.sety(-290)
    elif snake.head.ycor() < -290:
        snake.head.sety(290)

screen.exitonclick()