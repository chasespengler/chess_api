from . import models

#Returns boolean value determining if a piece is under attack or not given a row, column, and board
def under_attack(row, col, board):
    color = board[row][col][0]
    if color == '-':
        return False
    vectors = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    knight_vectors = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, 1)]
    for v, vector in enumerate(vectors):
        for i in range(1, 8):
            new_row = row + i*vector[0]
            new_col = col + i*vector[1]
            new_sq = board[new_row][new_col]
            if not allowed(new_row, new_col, board):
                break
            elif new_sq == '--':
                continue
            elif new_sq[0] == color:
                break
            elif new_sq[0] != color:
                if v <= 4 and (new_sq[1] == 'Q' or new_sq[1] == 'R'):
                    return True
                elif v > 4 and (new_sq[1] == 'Q' or new_sq[1] == 'B'):
                    return True
                elif color == 'w' and 4 < v < 7 and i == 1 and new_sq[1] == 'P':
                    return True
                elif color == 'b' and 6 < v and i == 1 and new_sq[1] == 'P':
                    return True

    for vector in knight_vectors:
        new_row = row + vector[0]
        new_col = col + vector[1]
        new_sq = board[new_row][new_col]
        if not allowed(new_row, new_col, board):
            continue
        elif new_sq[0] != color and new_sq[1] == 'N':
            return True

    return False


#Checks that a mvoe is in the constraints of the board and doesn't land on the piece's same color
def allowed(row, col, color, board):
    if row >= 8 or row < 0 or col >= 8 or col < 0:
        return False
    elif board[row][col][0] == color:
        return False
    else:
        return True

#Returns all moves for a pawn piece given a position and board
def get_pawn_moves(row, col, board):
    color = board[row][col][0]
    direction = {'w': 1, 'b': -1}
    moves = []
    if board[row + direction[color]][col] == '--':
        moves.append(models.move((row, col), (row + direction[color], col), board[row + direction[color]][col]))
    if ((row == 1 and color == 'w') or (row == 6 and color == 'b')) and board[row + direction[color]*2][col] == '--':
        moves.append(models.move((row, col), (row + direction[color]*2, col), board[row + direction[color]*2][col]))
    if (board[row + direction[color]][col + 1][0] != color and col != 7):
        moves.append(models.move((row, col), (row + direction[color], col + 1), board[row + direction[color]][col + 1]))
    if (board[row + direction[color]][col - 1][0] != color and col != 0):
        moves.append(models.move((row, col), (row + direction[color], col - 1), board[row + direction[color]][col - 1]))
    

#Returns all moves for a knight piece given a position and board
def get_knight_moves(row, col, board):
    color = board[row][col][0]
    moves = []
    vectors = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, 1)]
    for vector in vectors:
        new_row = row + vector[0]
        new_col = col + vector[1]
        if not allowed(new_row, new_col, color, board):
            continue
        else:
            moves.append(models.move((row, col), (new_row, new_col), board[new_row][new_col]))

    return moves

#Gets all potential moves for a rook piece given a position and board
def get_rook_moves(row, col, board):
    color = board[row][col][0]
    moves = []
    vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for vector in vectors:
        for i in range(1, 8):
            new_row = row + i*vector[0]
            new_col = row + i*vector[1]
            if not allowed(new_row, new_col, color, board):
                break
            else:
                moves.append(models.move((row, col), (new_row, new_col), board[new_row][new_col]))

    return moves

#Gets all potential moves for a bishop piece given a position and board
def get_bishop_moves(row, col, board):
    color = board[row][col][0]
    moves = []
    vectors = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for vector in vectors:
        for i in range(1, 8):
            new_row = row + i*vector[0]
            new_col = row + i*vector[1]
            if not allowed(new_row, new_col, color, board):
                break
            else:
                moves.append(models.move((row, col), (new_row, new_col), board[new_row][new_col]))

#Gets all potential moves for a queen piece given a position and board
def get_queen_moves(row, col, board):
    moves = get_rook_moves(row, col, board)
    moves.append(get_bishop_moves(row, col, board))
    return moves

#Gets all potential moves for a king piece given a position and board
def get_king_moves(row, col, board):
    color = board[row][col][0]
    moves = []
    vectors = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for vector in vectors:
        new_row = row + vector[0]
        new_col = col + vector[1]
        if not allowed(new_row, new_col, color, board):
            continue
        else:
            moves.append(models.move(row, col), (new_row, new_col), board[new_row][new_col])
    
    return moves

#Adds castle moves to kings moves
def add_castles():
    pass

#Removes moves resulting in own king being in check
def remove_check_moves():
    pass