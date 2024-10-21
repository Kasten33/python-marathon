from turtle import Screen
from board import Board
from score import Score
from pieces import Pieces
from player import Player

player = Player()
board = Board()
score = Score()
pieces = Pieces()

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Quick Chess")
screen.tracer(0)

def start():
        screen.update()
        board.generate()
        player.P1()
        player.P2()
        score.updateScore()
        pieces.generate()
        
screen.listen()
start()

On = True
while On:
    screen.update()





screen.exitonclick()
