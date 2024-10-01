from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(position)

    def start (self):
        self.goto(350, 0)

    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
        
    def reset(self):
        self.goto(350, 0)
        
    def move(self):
        pass

class Paddle2(Paddle):
    def __init__(self, position):
        super().__init__(position)
        self.goto(-350, 0)
    
    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)

    def reset(self):
        self.goto(-350, 0)
        
    def move(self):
        pass