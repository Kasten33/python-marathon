from turtle import Turtle
import time
from restrictions import Valid_Move, Move_Puts_King_In_Check

class Piece(Turtle):
    def __init__(self, shape, x, y, color, piece_type):
        super().__init__()
        self.shape(shape)
        self.penup()
        self.goto(x, y)
        self.color = color
        self.piece_type = piece_type  # Store the type of the piece
        

class Pieces:
    def __init__(self, player):
        self.pieces = []
        self.selected_piece = None
        self.original_position = None
        self.square_size = 75 
        self.last_move = None
        self.player = player

    def Add_Piece(self, shape, x, y, color, piece_type):
        snapped_x, snapped_y = self.Snap_Grid(x, y)
        piece = Piece(shape, snapped_x, snapped_y, color, piece_type)
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
        return True  # Legal move
    
    def Take_En_Passant(self, x, y, last_move):
        if last_move and last_move['piece'].piece_type == 'pawn' and abs(last_move['start_y'] - last_move['end_y']) == 2 * self.square_size:
            if last_move['end_x'] == x and last_move['end_y'] == y - self.square_size if self.selected_piece.color() == "light" else y + self.square_size:
                for piece in self.pieces:
                    if piece.xcor() == last_move['end_x'] and piece.ycor() == last_move['end_y']:
                        piece.hideturtle()
                        self.pieces.remove(piece)
                        return True
        return False

    def Flash_Red(self, x, y):
        red_square = Turtle()
        red_square.shape("square")
        red_square.color("red")
        red_square.penup()
        red_square.goto(x, y)
        time.sleep(0.2)
        red_square.hideturtle()

    def Selected_Move(self, x, y):
        if self.selected_piece:
            snapped_x, snapped_y = self.Snap_Grid(x, y)
            if Valid_Move(self.selected_piece, snapped_x, snapped_y, self.square_size, self.pieces, self.last_move):
                if not Move_Puts_King_In_Check(self.selected_piece, snapped_x, snapped_y, self.pieces, self.square_size, self.last_move):
                    if self.Take_Piece(snapped_x, snapped_y) or self.Take_En_Passant(snapped_x, snapped_y, self.last_move):
                        # Update last move
                        self.last_move = {
                            'piece': self.selected_piece,
                            'start_x': self.original_position[0],
                            'start_y': self.original_position[1],
                            'end_x': snapped_x,
                            'end_y': snapped_y
                        }
                        self.selected_piece.goto(snapped_x, snapped_y)
                        self.player.done = True  # Mark the move as done
                    else:
                        self.Flash_Red(self.original_position[0], self.original_position[1])
                        self.selected_piece.goto(self.original_position)
                else:
                    self.Flash_Red(self.original_position[0], self.original_position[1])
                    self.selected_piece.goto(self.original_position)
            else:
                self.Flash_Red(self.original_position[0], self.original_position[1])
                self.selected_piece.goto(self.original_position)
            self.selected_piece = None
        else:
            for piece in self.pieces:
                if piece.distance(x, y) < 20 and piece.color == self.player.current_turn_color():  # Check if the piece belongs to the current player
                    self.selected_piece = piece
                    self.original_position = (piece.xcor(), piece.ycor())
                    break

    def generate(self):
        # Light pieces
        for i in range(8):
            self.Add_Piece("imgs/LightPawn.gif", -262 + i * 75, -190, "light", "pawn")
        self.Add_Piece("imgs/LightRook.gif", -262, -264, "light", "rook")
        self.Add_Piece("imgs/LightRook.gif", 262, -264, "light", "rook")
        self.Add_Piece("imgs/LightKnight.gif", -188, -264, "light", "knight")
        self.Add_Piece("imgs/LightKnight.gif", 188, -264, "light", "knight")
        self.Add_Piece("imgs/LightBishop.gif", -112, -264, "light", "bishop")
        self.Add_Piece("imgs/LightBishop.gif", 112, -264, "light", "bishop")
        self.Add_Piece("imgs/LightQueen.gif", 38, -264, "light", "queen")
        self.Add_Piece("imgs/LightKing.gif", -38, -264, "light", "king")

        # Dark pieces
        for i in range(8):
            self.Add_Piece("imgs/DarkPawn.gif", -262 + i * 75, 190, "dark", "pawn")
        self.Add_Piece("imgs/DarkRook.gif", -262, 264, "dark", "rook")
        self.Add_Piece("imgs/DarkRook.gif", 262, 264, "dark", "rook")
        self.Add_Piece("imgs/DarkKnight.gif", -188, 264, "dark", "knight")
        self.Add_Piece("imgs/DarkKnight.gif", 188, 264, "dark", "knight")
        self.Add_Piece("imgs/DarkBishop.gif", -112, 264, "dark", "bishop")
        self.Add_Piece("imgs/DarkBishop.gif", 112, 264, "dark", "bishop")
        self.Add_Piece("imgs/DarkQueen.gif", 38, 264, "dark", "queen")
        self.Add_Piece("imgs/DarkKing.gif", -38, 264, "dark", "king")