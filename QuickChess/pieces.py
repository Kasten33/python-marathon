from turtle import Turtle, Screen
import time

class Piece(Turtle):
    def __init__(self, shape, x, y, color):
        super().__init__()
        self.shape(shape)
        self.penup()
        self.goto(x, y)
        self.color = color
    
class Pieces:
        def __init__(self):
            self.pieces = []
            self.selected_piece = None
            self.square_size = 75

        def Add_Piece(self, shape, x, y, color):
            snapped_x, snapped_y = self.Snap_Grid(x, y)
            piece = Piece(shape, snapped_x, snapped_y, color)
            self.pieces.append(piece)

        def Snap_Grid(self, x, y):
            snapped_x = round((x + self.square_size / 2) / self.square_size) * self.square_size - self.square_size / 2
            snapped_y = round((y + self.square_size / 2) / self.square_size) * self.square_size - self.square_size / 2
            return snapped_x, snapped_y
        
        def Take_Piece(self, x, y):
                for piece in self.pieces:
                    if piece.xcor() == x and piece.ycor() == y:
                        if piece.color != self.selected_piece.color:
                            piece.hideturtle()
                            self.pieces.remove(piece)
                        else:
                            return False  # Illegal move
                        break
                return True

        def Flash_Red(self, x, y):
            screen = Screen()
            original_color = screen.bgcolor()
            screen.bgcolor("red")
            screen.update()
            time.sleep(0.2)
            screen.bgcolor(original_color)
            screen.update()

        def Selected_Move(self, x, y):
            if self.selected_piece:
                snapped_x, snapped_y = self.Snap_Grid(x, y)
                if self.Take_Piece(snapped_x, snapped_y):
                    self.selected_piece.goto(snapped_x, snapped_y)
                else:
                    self.Flash_Red(self.original_position[0], self.original_position[1])
                    self.selected_piece.goto(self.original_position)
                self.selected_piece = None
            else:
                for piece in self.pieces:
                    if piece.distance(x, y) < 20: 
                        self.selected_piece = piece
                        self.original_position = (piece.xcor(), piece.ycor())
                        break

        def generate(self):
            # Light pieces
            for i in range(8):
                self.Add_Piece("imgs/LightPawn.gif", -262 + i * 75, -190, "light")
            self.Add_Piece("imgs/LightRook.gif", -262, -264, "light")
            self.Add_Piece("imgs/LightRook.gif", 262, -264, "light")
            self.Add_Piece("imgs/LightKnight.gif", -188, -264, "light")
            self.Add_Piece("imgs/LightKnight.gif", 188, -264, "light")
            self.Add_Piece("imgs/LightBishop.gif", -112, -264, "light")
            self.Add_Piece("imgs/LightBishop.gif", 112, -264, "light")
            self.Add_Piece("imgs/LightQueen.gif", 38, -264, "light")
            self.Add_Piece("imgs/LightKing.gif", -38, -264, "light")

            # Dark pieces
            for i in range(8):
                self.Add_Piece("imgs/DarkPawn.gif", -262 + i * 75, 190, "dark")
            self.Add_Piece("imgs/DarkRook.gif", -262, 264, "dark")
            self.Add_Piece("imgs/DarkRook.gif", 262, 264, "dark")
            self.Add_Piece("imgs/DarkKnight.gif", -188, 264, "dark")
            self.Add_Piece("imgs/DarkKnight.gif", 188, 264, "dark")
            self.Add_Piece("imgs/DarkBishop.gif", -112, 264, "dark")
            self.Add_Piece("imgs/DarkBishop.gif", 112, 264, "dark")
            self.Add_Piece("imgs/DarkQueen.gif", 38, 264, "dark")
            self.Add_Piece("imgs/DarkKing.gif", -38, 264, "dark")
