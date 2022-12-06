from . import models
from . import board_dynamics
make_move = board_dynamics.make_move

#Gets all moves
def get_moves(row, col, color, board):
    move_dict = {'P': get_pawn_moves, 'R': get_rook_moves, 'N': get_knight_moves, 'B': get_bishop_moves, 'Q': get_queen_moves, 'K': get_king_moves}
    piece = board[row][col]
    if piece == '--':
        return
    moves = move_dict[piece[1]](row, col, color, board)
    return moves

#Returns boolean value determining if a piece is under attack or not given a color, row, column, and board
def under_attack(row, col, color, board):
    vectors = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    knight_vectors = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, 1)]
    for v, vector in enumerate(vectors):
        for i in range(1, 8):
            new_row = row + i*vector[0]
            new_col = col + i*vector[1]
            if allowed(new_row, new_col, color, board):
                new_sq = board[new_row][new_col]
            else:
                break
            if new_sq == '--':
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
        if allowed(new_row, new_col, color, board):
            new_sq = board[new_row][new_col]
        else:
            continue
        if new_sq[0] != color and new_sq[1] == 'N':
            return True

    return False


#Checks that a mvoe is in the constraints of the board and doesn't land on the piece's same color
def allowed(row, col, color, board):
    if row >= 8 or row < 0 or col >= 8 or col < 0:
        return False
    elif board[row][col][0] == color:
        return False
    return True

#Returns all moves for a pawn piece given a position and board
def get_pawn_moves(row, col, color, board):
    direction = {'w': 1, 'b': -1}
    moves = []
    # print('!'*100)
    # print(row, col)
    # print(row + direction[color])
    # print('!'*100)
    if board[row + direction[color]][col] == '--':
        move = models.move((row, col), (row + direction[color], col), board[row + direction[color]][col], board)
        if not own_check_moves(color, board, move):
            moves.append(move)
    if ((row == 1 and color == 'w') or (row == 6 and color == 'b')) and board[row + direction[color]*2][col] == '--':
        move = models.move((row, col), (row + direction[color]*2, col), board[row + direction[color]*2][col], board)
        if not own_check_moves(color, board, move):
            moves.append(move)
    if (col != 7 and board[row + direction[color]][col + 1][0] != color):
        move = models.move((row, col), (row + direction[color], col + 1), board[row + direction[color]][col + 1], board)
        if not own_check_moves(color, board, move):
            moves.append(move)
    if (col != 0 and board[row + direction[color]][col - 1][0] != color):
        move = models.move((row, col), (row + direction[color], col - 1), board[row + direction[color]][col - 1], board)
        if not own_check_moves(color, board, move):
            moves.append(move)
    
    if moves:
        return moves
    return
    

#Returns all moves for a knight piece given a position and board
def get_knight_moves(row, col, color, board):
    moves = []
    vectors = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, 1)]
    for vector in vectors:
        new_row = row + vector[0]
        new_col = col + vector[1]
        if not allowed(new_row, new_col, color, board):
            continue
        elif own_check_moves(color, board, models.move((row, col), (new_row, new_col), board[new_row][new_col], board)):
            return
        else:
            moves.append(models.move((row, col), (new_row, new_col), board[new_row][new_col], board))

    return moves

#Gets all potential moves for a rook piece given a position and board
def get_rook_moves(row, col, color, board):
    moves = []
    vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for vector in vectors:
        for i in range(1, 8):
            new_row = row + i*vector[0]
            new_col = row + i*vector[1]
            if not allowed(new_row, new_col, color, board):
                break
            elif own_check_moves(color, board, models.move((row, col), (new_row, new_col), board[new_row][new_col], board)):
                continue
            else:
                moves.append(models.move((row, col), (new_row, new_col), board[new_row][new_col], board))
    if moves:
        return moves
    return

#Gets all potential moves for a bishop piece given a position and board
def get_bishop_moves(row, col, color, board):
    moves = []
    vectors = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for vector in vectors:
        for i in range(1, 8):
            new_row = row + i*vector[0]
            new_col = row + i*vector[1]
            if not allowed(new_row, new_col, color, board):
                break
            elif own_check_moves(color, board, models.move((row, col), (new_row, new_col), board[new_row][new_col], board)):
                continue           
            else:
                moves.append(models.move((row, col), (new_row, new_col), board[new_row][new_col], board))
    
    return moves

#Gets all potential moves for a queen piece given a position and board
def get_queen_moves(row, col, color, board):
    r_moves = get_rook_moves(row, col, color, board)
    moves = r_moves.extend(get_bishop_moves(row, col, color, board)) if r_moves else get_bishop_moves(row, col, color, board)
    if moves:
        return moves
    return

#Gets all potential moves for a king piece given a position and board
def get_king_moves(row, col, color, board):
    moves = []
    vectors = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for vector in vectors:
        new_row = row + vector[0]
        new_col = col + vector[1]
        if not allowed(new_row, new_col, color, board):
            continue
        if under_attack(new_row, new_col, color, board):
            continue
        else:
            move = models.move((row, col), (new_row, new_col), board[new_row][new_col], board)
            moves.append(move)
    
    if moves:
        return moves
    return

#Adds castle moves
def add_castles(color, castleability, board):
    moves = []
    if not castleability:
        return moves
    if color == 'w':
        if 'wQs' in castleability:
            if board[0][4] == '--' and board[0][5] == '--' and board[0][5] == '--':
                if not under_attack(0, 4, 'w', board) and not under_attack(0, 5, 'w', board) and not under_attack(0, 6, 'w', board):
                    moves.append(models.move((0, 3), (0, 5), '--', board, is_castle=True, castle_type='wQs'))
        if 'wKs' in castleability:
            if board[0][2] == '--' and board[0][1] == '--':
                if not under_attack(0, 2, 'w', board) and not under_attack(0, 1, 'w', board):
                    moves.append(models.move((0, 3), (0, 1), '--', board, is_castle=True, castle_type='wKs'))
    else:
        if 'bQs' in castleability:
            if board[7][4] == '--' and board[7][5] == '--' and board[7][6] == '--':
                if not under_attack(7, 4, 'b', board) and not under_attack(7, 5, 'b', board) and not under_attack(7, 6, 'b', board):
                    moves.append(models.move((7, 3), (7, 5), '--', board, is_castle=True, castle_type='bQs'))
        if 'bKs' in castleability:
            if board[7][2] == '--' and board[7][1] == '--':
                if not under_attack(7, 2, 'b', board) and not under_attack(7, 1, 'b', board):
                    moves.append(models.move((7, 3), (7, 1), '--', board, is_castle=True, castle_type='bKs'))

    if moves:
        return moves
    return

#Checks for moves resulting in own king being in check
def own_check_moves(color, board, move):
    for r, row in enumerate(board):
        if color + 'K' in row:
            kings_location = (r, row.index(color+'K'))
            break

    new_board = make_move(board, move)
    if under_attack(kings_location[0], kings_location[1], color, new_board):
        return True

    return False
