from turtle import Screen
from PIL import Image

def register(screen: Screen):


    # Light pieces
    screen.addshape("imgs/LightPawn.gif")
    screen.addshape("imgs/LightRook.gif")
    screen.addshape("imgs/LightKing.gif")
    screen.addshape("imgs/LightQueen.gif")
    screen.addshape("imgs/LightBishop.gif")
    screen.addshape("imgs/LightKnight.gif")

    # Dark pieces
    screen.addshape("imgs/DarkPawn.gif")
    screen.addshape("imgs/DarkRook.gif")
    screen.addshape("imgs/DarkKing.gif")
    screen.addshape("imgs/DarkQueen.gif")
    screen.addshape("imgs/DarkBishop.gif")
    screen.addshape("imgs/DarkKnight.gif")