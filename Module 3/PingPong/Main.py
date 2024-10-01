from turtle import Screen
from Paddle import Paddle, Paddle2
from Ball import Ball
from SBoard import SBoard
import time

ball = Ball()
sBoard = SBoard()
paddle = Paddle((350, 0))
paddle2 = Paddle2((-350, 0))



# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # Turn off screen updates


screen.listen()
screen.onkeypress(paddle.up, "Up")
screen.onkeypress(paddle.down, "Down")
screen.onkeypress(paddle2.up, "w")
screen.onkeypress(paddle2.down, "s")

#Main game loop
On = True
while On:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.xcor() > 390:
        ball.reset()
        paddle.reset()
        paddle2.reset()
        sBoard.l_point()
        

    if ball.xcor() < -390:
        ball.reset()
        paddle.reset()
        paddle2.reset()
        sBoard.r_point()

    if (ball.distance(paddle) < 50 and ball.xcor() > 340) or (ball.distance(paddle2) < 50 and ball.xcor() < -340):
        ball.bounce_x()
    if sBoard.l_score == 5 or sBoard.r_score == 5:
        On = False
        sBoard.game_over()
        if sBoard.l_score == 5:
            sBoard.goto(-100, 0)
            sBoard.write("Left Player Wins", align="left", font=("Courier", 80, "normal"))
        else:
            sBoard.goto(100, 0)
            sBoard.write("Right Player Wins", align="right", font=("Courier", 10, "normal"))



screen.exitonclick()