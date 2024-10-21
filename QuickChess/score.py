from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.goto(-130, 300)
        self.write(self.l_score, align="center", font=("Courier", 24, "normal"))
        self.goto(295, -335)
        self.write(self.r_score, align="center", font=("Courier", 24, "normal"))

    def l_point(self):
        self.l_score += 1
        self.updateScore()

    def r_point(self):
        self.r_score += 1
        self.updateScore()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", color="red", align="center", font=("Courier", 80, "normal"))