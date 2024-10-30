from turtle import Screen
from board import Board
from score import Score
from pieces import Pieces
from player import Player
from register import register
from restrictions import Is_King_In_Check, Is_Checkmate

player = Player()
board = Board()
score = Score()
pieces = Pieces(player)

screen = Screen()
register(screen)

screen.setup(width=700, height=690)
screen.bgcolor("black")
screen.title("Quick Chess")
screen.tracer(0)

screen.onclick(pieces.Selected_Move, 1)

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
    

        # Check if the king is in check or checkmate
    for piece in pieces.pieces:
        if piece.piece_type == "king":
            if Is_King_In_Check(piece, pieces.pieces, pieces.square_size):
                print(f"{piece.color} king is in check!")
                if Is_Checkmate(piece, pieces.pieces, pieces.square_size):
                    print(f"{piece.color} king is in checkmate!")
                    if piece.color == "light":
                        score.r_point()
                    else:
                        score.l_point()
                if score.l_score == 3 or score.r_score == 3:
                    score.game_over()
                    On = False
                    break
    if pieces.selected_piece is None and player.done:
        player.switch_turn()
        player.done = False
        
                
screen.exitonclick()