from turtle import Turtle
class Pieces(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()

    def Pawn(self):
        self.goto(300,50)
    def King(self):
        self.goto(300,0)
    def Queen(self):
        self.goto(300,-50)
    def Bishop(self):
        self.goto(300,-100)
    def Knight(self):
        self.goto(300,-150)
    def Rook(self):
        self.goto(300,-200)
    def generate(self):
        for i in range(8):
            self.Pawn()
            self.King()
            self.Queen()
            self.Bishop()
            self.Knight()
            self.Rook()
