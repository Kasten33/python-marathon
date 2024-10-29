from turtle import Turtle, Screen
class Pieces(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
    def Pawn(self):
        self.shape("imgs/LightPawn.gif")
        self.goto(-338, -190)
        for i in range(8):
            self.goto(self.xcor()+75, self.ycor())
            self.stamp()
    def Pawn2(self):
        self.shape("imgs/DarkPawn.gif")
        self.goto(-338, 190)
        for i in range(8):
            self.goto(self.xcor()+75, self.ycor())
            self.stamp()
    def King(self):
        self.shape("imgs/LightKing.gif")
        self.goto(-38, -265)
        self.stamp()
    def King2(self):
        self.shape("imgs/DarkKing.gif")
        self.goto(-38, 265)
        self.stamp()
    def Queen(self):
        self.shape("imgs/LightQueen.gif")
        self.goto(38, -265)
        self.stamp()
    def Queen2(self):
        self.shape("imgs/DarkQueen.gif")
        self.goto(38, 265)
        self.stamp()
    def Bishop(self):
        self.shape("imgs/LightBishop.gif")
        self.goto(-112, -265)
        self.stamp()
        self.penup()
        self.goto(112, -265)
        self.stamp()
    def Bishop2(self):
        self.shape("imgs/DarkBishop.gif")
        self.goto(-112, 265)
        self.stamp()
        self.penup()
        self.goto(112, 265)
        self.stamp()
    def Knight(self):
        self.shape("imgs/LightKnight.gif")
        self.goto(-188, -265)
        self.stamp()
        self.penup()
        self.goto(188, -265)
        self.stamp()
    def Knight2(self):
        self.shape("imgs/DarkKnight.gif")
        self.goto(-188, 265)
        self.stamp()
        self.penup()
        self.goto(188, 265)
        self.stamp()
    def Rook(self):
        self.shape("imgs/LightRook.gif")
        self.goto(-262, -265)
        self.stamp()
        self.penup()
        self.goto(262, -265)
        self.stamp()
    def Rook2(self):
        self.shape("imgs/DarkRook.gif")
        self.goto(-262, 265)
        self.stamp()
        self.penup()
        self.goto(262, 265)

            
    def generate(self):
        self.Pawn()
        self.Pawn2()
        self.King()
        self.King2()
        self.Queen()
        self.Queen2()
        self.Bishop()
        self.Bishop2()
        self.Knight()
        self.Knight2()
        self.Rook()
        self.Rook2()

