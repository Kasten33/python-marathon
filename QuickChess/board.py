from turtle import Turtle
class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.goto(-300, 300)

    def generate(self):
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0:
                    self.color("white")
                else:
                    self.color("green")
                self.begin_fill()
                for _ in range(4):
                    self.forward(75)
                    self.right(90)
                self.end_fill()
                self.forward(75)
            self.goto(-300, self.ycor()-75)
       
        