from turtle import Turtle
class Pieces(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

    def Pawn(self):
        self.goto(300,50)

    def King(self):
        self.goto(300,0)
