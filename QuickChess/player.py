from turtle import Turtle
class Player(Turtle):
    def __init__ (self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.turn = "Player 1"
        self.done = False


        
    def P1(self):
        self.color("blue")
        self.goto(200, -335)
        self.write("Player 1", align="center", font=("Courier", 24, "normal"))

    def P2(self):
        self.color("red")
        self.goto(-225, 300)
        self.write("Player 2", align="center", font=("Courier", 24, "normal"))

    def first_turn(self):
        self.turn = "Player 1"
        self.done = False

    def switch_turn(self):
        if self.turn == "Player 1":
            self.turn = "Player 2"
        else:
            self.turn = "Player 1"
        self.done = False  # Reset the done attribute after switching turns

    def current_turn_color(self):
        if self.turn == "Player 1":
            return "light"
        else:
            return "dark"

    def current_turn(self):
        return self.turn