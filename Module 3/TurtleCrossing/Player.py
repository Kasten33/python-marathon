from turtle import Turtle

class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def l(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def r(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

