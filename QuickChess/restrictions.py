def Within_Bounds(x, y):
    return -300 <= x <= 300 and -300 <= y <= 300

def Snap_Grid(x, y, square_size):
    snapped_x = round((x + square_size / 2) / square_size) * square_size - square_size / 2
    snapped_y = round((y + square_size / 2) / square_size) * square_size - square_size / 2
    return snapped_x, snapped_y

def Valid_Pawn(piece, x, y, square_size, pieces, last_move):
    if not Within_Bounds(x, y):
        return False

    dx = abs(x - piece.xcor())
    dy = y - piece.ycor() if piece.color == "light" else piece.ycor() - y 
    if piece.color == "light":
        initial_row = Snap_Grid(0, -262 + square_size, square_size)[1]  # Center of the second row from the bottom
        direction = square_size
    else:
        initial_row = Snap_Grid(0, 262 - square_size, square_size)[1]  # Center of the second row from the top
        direction = -square_size

    # Check if the square directly in front of the pawn is occupied
    if dx == 0:
        front_x = piece.xcor()
        front_y = piece.ycor() + direction
        for p in pieces:
            if p.xcor() == front_x and p.ycor() == front_y:
                return False

    # Initial two-square move
    if piece.ycor() == initial_row and dx == 0 and dy == 2 * square_size:
        # Check if both squares in front of the pawn are unoccupied
        front_y = piece.ycor() + direction
        front_y_two = piece.ycor() + 2 * direction
        if not any(p.xcor() == front_x and p.ycor() == front_y for p in pieces) and \
           not any(p.xcor() == front_x and p.ycor() == front_y_two for p in pieces):
            return True

    # Regular one-square move
    if dx == 0 and dy == square_size:
        # Check if the square directly in front of the pawn is unoccupied
        front_x = piece.xcor()
        front_y = piece.ycor() + direction
        if not any(p.xcor() == front_x and p.ycor() == front_y for p in pieces):
            return True
    
    # Capture move
    if dx == square_size and dy == square_size:
        for p in pieces:
            if p.xcor() == x and p.ycor() == y and p.color != piece.color:
                return True

    # En passant move
    if dx == square_size and dy == square_size:
        if last_move and last_move['piece'].piece_type == 'pawn' and abs(last_move['start_y'] - last_move['end_y']) == 2 * square_size:
            if last_move['end_x'] == x and last_move['end_y'] == piece.ycor():
                return True

    return False

def Path_Clear(piece, x, y, pieces, square_size):
    if piece.piece_type in ["rook", "queen"]:
        if not Straight_Path_Clear(piece, x, y, pieces, square_size):
            return False
    if piece.piece_type in ["bishop", "queen"]:
        if not Diagonal_Path_Clear(piece, x, y, pieces, square_size):
            return False
    return True

def Straight_Path_Clear(piece, x, y, pieces, square_size):
    if piece.xcor() == x:
        step = square_size if y > piece.ycor() else -square_size
        for pos in range(int(piece.ycor() + step), int(y), step):
            snapped_x, snapped_y = Snap_Grid(x, pos, square_size)
            if any(p.xcor() == snapped_x and p.ycor() == snapped_y for p in pieces):
                return False
    elif piece.ycor() == y:
        step = square_size if x > piece.xcor() else -square_size
        for pos in range(int(piece.xcor() + step), int(x), step):
            snapped_x, snapped_y = Snap_Grid(pos, y, square_size)
            if any(p.xcor() == snapped_x and p.ycor() == snapped_y for p in pieces):
                return False
    return True

def Diagonal_Path_Clear(piece, x, y, pieces, square_size):
    step_x = square_size if x > piece.xcor() else -square_size
    step_y = square_size if y > piece.ycor() else -square_size
    for pos_x, pos_y in zip(range(int(piece.xcor() + step_x), int(x), step_x),
                            range(int(piece.ycor() + step_y), int(y), step_y)):
        snapped_x, snapped_y = Snap_Grid(pos_x, pos_y, square_size)
        if any(p.xcor() == snapped_x and p.ycor() == snapped_y for p in pieces):
            return False
    return True

def Valid_Rook(piece, x, y, square_size, pieces, last_move):
    dx = abs(x - piece.xcor())
    dy = abs(y - piece.ycor())
    if dx == 0 or dy == 0:
        return Path_Clear(piece, x, y, pieces, square_size)
    return False

def Valid_Bishop(piece, x, y, square_size, pieces, last_move):
    dx = abs(x - piece.xcor())
    dy = abs(y - piece.ycor())
    if dx == dy:
        return Path_Clear(piece, x, y, pieces, square_size)
    return False

def Valid_Queen(piece, x, y, square_size, pieces, last_move):
    dx = abs(x - piece.xcor())
    dy = abs(y - piece.ycor())
    if dx == dy or dx == 0 or dy == 0:
        return Path_Clear(piece, x, y, pieces, square_size)
    return False

def Valid_Knight(piece, x, y, square_size, pieces, last_move):
    if not Within_Bounds(x, y):
        return False

    dx = abs(x - piece.xcor())
    dy = abs(y - piece.ycor())
    return (dx == square_size * 2 and dy == square_size) or (dx == square_size and dy == square_size * 2)

def Valid_King(piece, x, y, square_size, pieces, last_move):
    if not Within_Bounds(x, y):
        return False

    dx = abs(x - piece.xcor())
    dy = abs(y - piece.ycor())
    return dx <= square_size and dy <= square_size

def Is_King_In_Check(king, pieces, square_size):
    for piece in pieces:
        if piece.color != king.color:
            if Valid_Move(piece, king.xcor(), king.ycor(), square_size, pieces, None):
                return True
    return False

def Can_King_Escape(king, pieces, square_size):
    directions = [(square_size, 0), (-square_size, 0), (0, square_size), (0, -square_size),
                  (square_size, square_size), (square_size, -square_size), (-square_size, square_size), (-square_size, -square_size)]
    for dx, dy in directions:
        new_x = king.xcor() + dx
        new_y = king.ycor() + dy
        snapped_x, snapped_y = Snap_Grid(new_x, new_y, square_size)
        if Within_Bounds(snapped_x, snapped_y):
            if not Move_Puts_King_In_Check(king, snapped_x, snapped_y, pieces, square_size, None):
                return True
    return False

def Is_Checkmate(king, pieces, square_size):
    if Is_King_In_Check(king, pieces, square_size):
        if not Can_King_Escape(king, pieces, square_size):
            # Check if any piece can block the check or capture the attacking piece
            for piece in pieces:
                if piece.color == king.color:
                    original_x, original_y = piece.xcor(), piece.ycor()
                    for x in range(-300, 301, square_size):
                        for y in range(-300, 301, square_size):
                            snapped_x, snapped_y = Snap_Grid(x, y, square_size)
                            if Valid_Move(piece, snapped_x, snapped_y, square_size, pieces, None):
                                piece.goto(snapped_x, snapped_y)
                                if not Is_King_In_Check(king, pieces, square_size):
                                    piece.goto(original_x, original_y)
                                    return False
                                piece.goto(original_x, original_y)
            return True
    return False

def Move_Puts_King_In_Check(piece, x, y, pieces, square_size, last_move):
    # Simulate the move
    original_x, original_y = piece.xcor(), piece.ycor()
    piece.goto(x, y)
    king = next(p for p in pieces if p.piece_type == "king" and p.color == piece.color)
    in_check = Is_King_In_Check(king, pieces, square_size)
    # Undo the move
    piece.goto(original_x, original_y)
    return in_check

def Valid_Move(piece, x, y, square_size, pieces, last_move):
    if piece.piece_type == "pawn":
        return Valid_Pawn(piece, x, y, square_size, pieces, last_move)
    elif piece.piece_type == "rook":
        return Valid_Rook(piece, x, y, square_size, pieces, last_move)
    elif piece.piece_type == "knight":
        return Valid_Knight(piece, x, y, square_size, pieces, last_move)
    elif piece.piece_type == "bishop":
        return Valid_Bishop(piece, x, y, square_size, pieces, last_move)
    elif piece.piece_type == "queen":
        return Valid_Queen(piece, x, y, square_size, pieces, last_move)
    elif piece.piece_type == "king":
        return Valid_King(piece, x, y, square_size, pieces, last_move) 
    return False