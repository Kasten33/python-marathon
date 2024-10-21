from turtle import Turtle
class Player(Turtle):
    def __init__ (self):
        super().__init__()
        self.penup()
        self.shape("square")
        
    def P1(self):
        self.write("Player 1", align="center", font=("Courier", 24, "normal"))
        self.goto(-300,0)
        self.color("white")

    def P2(self):
        self.write("Player 2", align="center", font=("Courier", 24, "normal"))
        self.goto(300,0)
        self.color("black")
