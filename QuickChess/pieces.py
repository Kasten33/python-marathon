from turtle import Turtle, Screen
class Pieces(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
    def Pawn(self):
        self.shape("imgs/LightPawn.gif")
        self.goto(-338, 190)
        for i in range(8):
            self.goto(self.xcor()+75, self.ycor())
            self.stamp()
    def Pawn2(self):
        self.shape("imgs/DarkPawn.gif")
        self.goto(-338, -190)
        for i in range(8):
            self.goto(self.xcor()+75, self.ycor())
            self.stamp()
    def generate(self):
        self.Pawn()
        self.Pawn2()
