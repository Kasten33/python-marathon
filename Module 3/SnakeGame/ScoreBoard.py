from turtle import Turtle
class SBoard(Turtle):

    def __init__ (self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.color("white")

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.color("red")
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
      
        
       
