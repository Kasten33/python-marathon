from turtle import Turtle
class Player(Turtle):
    def __init__ (self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("square")
        
    def P1(self):
        self.color("blue")
        self.goto(-225,300)
        self.write("Player 1", align="center", font=("Courier", 24, "normal"))
        
        

    def P2(self):
        self.color("red")
        self.goto(200,-335)
        self.write("Player 2", align="center", font=("Courier", 24,  "normal"))
        
        
