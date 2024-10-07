from turtle import Turtle

class SBoard1(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 0  # Initialize level
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()  # Clear previous text
        self.goto(-400, 450)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def increase_level(self):
        self.level += 1
        self.updateScoreboard()
    def gameO(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 80, "normal"))