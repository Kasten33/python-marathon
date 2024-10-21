from turtle import Turtle, Screen
class Pieces(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
    def Pawn(self):
        self.shape("imgs/pawn1.gif")
        self.goto(-300, 225)
        for i in range(8):
            self.goto(self.xcor()+75, self.ycor())
            self.stamp()
    def Pawn2(self):
        self.shape("imgs/pawn2.gif")
        self.goto(-300, -225)
        for i in range(8):
            self.goto(self.xcor()+75, self.ycor())
            self.stamp()
    def generate(self):
        self.Pawn()
        self.Pawn2()
