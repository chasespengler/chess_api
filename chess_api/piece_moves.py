from . import models
from . import board_dynamics
make_move = board_dynamics.make_move

#Gets moves given board and color
def get_board_moves(board, color, checks):
    moves = []
    for r, row in enumerate(board):
        for c, piece in enumerate(row):
            if piece[0] == color:
                new_moves = get_moves(r, c, color, board, checks)
                if new_moves:
                    moves.extend(new_moves)

    return moves

#Gets all moves of a given square
def get_moves(row, col, color, board, checks):
    move_dict = {'P': get_pawn_moves, 'R': get_rook_moves, 'N': get_knight_moves, 'B': get_bishop_moves, 'Q': get_queen_moves, 'K': get_king_moves}
    piece = board[row][col]
    if piece == '--':
        return
    moves = move_dict[piece[1]](row, col, color, board, checks)
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
                elif color == 'w' and 3 < v < 6 and i == 1 and new_sq[1] == 'P':
                    return True
                elif color == 'b' and 5 < v and i == 1 and new_sq[1] == 'P':
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
def get_pawn_moves(row, col, color, board, checks):
    direction = {'w': 1, 'b': -1}
    moves = []
    if board[row + direction[color]][col] == '--':
        move = models.move((row, col), (row + direction[color], col), board[row + direction[color]][col], board)
        if not own_check_moves(color, board, move):
            if move.end[0] == 7 and color == 'w':
                move.is_promotion = True
            elif move.end[0] == 0 and color == 'b':
                move.is_promotion = True
            if checks:
                moves.append(checks_and_checkmate(color, board, move))
            else:
                moves.append(move)
    if ((row == 1 and color == 'w') or (row == 6 and color == 'b')) and board[row + direction[color]*2][col] == '--':
        move = models.move((row, col), (row + direction[color]*2, col), board[row + direction[color]*2][col], board)
        if not own_check_moves(color, board, move):
            if move.end[0] == 7 and color == 'w':
                move.is_promotion = True
            elif move.end[0] == 0 and color == 'b':
                move.is_promotion = True
            if checks:
                moves.append(checks_and_checkmate(color, board, move))
            else:
                moves.append(move)
    if (col != 7 and board[row + direction[color]][col + 1][0] != color and board[row + direction[color]][col + 1][0] != '-'):
        move = models.move((row, col), (row + direction[color], col + 1), board[row + direction[color]][col + 1], board)
        if not own_check_moves(color, board, move):
            if move.end[0] == 7 and color == 'w':
                move.is_promotion = True
            elif move.end[0] == 0 and color == 'b':
                move.is_promotion = True
            if checks:
                moves.append(checks_and_checkmate(color, board, move))
            else:
                moves.append(move)
    if (col != 0 and board[row + direction[color]][col - 1][0] != color and board[row + direction[color]][col - 1][0] != '-'):
        move = models.move((row, col), (row + direction[color], col - 1), board[row + direction[color]][col - 1], board)
        if not own_check_moves(color, board, move):
            if move.end[0] == 7 and color == 'w':
                move.is_promotion = True
            elif move.end[0] == 0 and color == 'b':
                move.is_promotion = True
            if checks:
                moves.append(checks_and_checkmate(color, board, move))
            else:
                moves.append(move)
    
    if moves:
        return moves
    return
    

#Returns all moves for a knight piece given a position and board
def get_knight_moves(row, col, color, board, checks):
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
            move = models.move((row, col), (new_row, new_col), board[new_row][new_col], board)
            if checks:
                moves.append(checks_and_checkmate(color, board, move))
            else:
                moves.append(move)

    return moves

#Gets all potential moves for a rook piece given a position and board
def get_rook_moves(row, col, color, board, checks):
    moves = []
    vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for vector in vectors:
        for i in range(1, 8):
            new_row = row + i*vector[0]
            new_col = col + i*vector[1]
            if not allowed(new_row, new_col, color, board):
                break
            elif own_check_moves(color, board, models.move((row, col), (new_row, new_col), board[new_row][new_col], board)):
                continue
            else:
                move = models.move((row, col), (new_row, new_col), board[new_row][new_col], board)
                if checks:
                    moves.append(checks_and_checkmate(color, board, move))
                else:
                    moves.append(move)
    if moves:
        return moves
    return

#Gets all potential moves for a bishop piece given a position and board
def get_bishop_moves(row, col, color, board, checks):
    moves = []
    vectors = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for vector in vectors:
        for i in range(1, 8):
            new_row = row + i*vector[0]
            new_col = col + i*vector[1]
            if not allowed(new_row, new_col, color, board):
                break
            elif own_check_moves(color, board, models.move((row, col), (new_row, new_col), board[new_row][new_col], board)):
                continue           
            else:
                move = models.move((row, col), (new_row, new_col), board[new_row][new_col], board)
                if checks:
                    moves.append(checks_and_checkmate(color, board, move))
                moves.append(move)
    
    return moves

#Gets all potential moves for a queen piece given a position and board
def get_queen_moves(row, col, color, board, checks):
    r_moves = get_rook_moves(row, col, color, board, checks)
    moves = r_moves.extend(get_bishop_moves(row, col, color, board, checks)) if r_moves else get_bishop_moves(row, col, color, board, checks)
    if moves:
        return moves
    return

#Gets all potential moves for a king piece given a position and board
def get_king_moves(row, col, color, board, checks):
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
                    move = models.move((0, 3), (0, 5), '--', board, is_castle=True, castle_type='wQs')
                    moves.append(checks_and_checkmate(color, board, move))
        if 'wKs' in castleability:
            if board[0][2] == '--' and board[0][1] == '--':
                if not under_attack(0, 2, 'w', board) and not under_attack(0, 1, 'w', board):
                    move = models.move((0, 3), (0, 1), '--', board, is_castle=True, castle_type='wKs')
                    moves.append(checks_and_checkmate(color, board, move))
    else:
        if 'bQs' in castleability:
            if board[7][4] == '--' and board[7][5] == '--' and board[7][6] == '--':
                if not under_attack(7, 4, 'b', board) and not under_attack(7, 5, 'b', board) and not under_attack(7, 6, 'b', board):
                    move = models.move((7, 3), (7, 5), '--', board, is_castle=True, castle_type='bQs')
                    moves.append(color, board, move)
        if 'bKs' in castleability:
            if board[7][2] == '--' and board[7][1] == '--':
                if not under_attack(7, 2, 'b', board) and not under_attack(7, 1, 'b', board):
                    move = models.move((7, 3), (7, 1), '--', board, is_castle=True, castle_type='bKs')
                    moves.append(color, board, move)

    if moves:
        return moves
    return

#Checks for moves resulting in own king being in check
def own_check_moves(color, board, move):
    kings_location = False
    for r, row in enumerate(board):
        if color + 'K' in row:
            kings_location = (r, row.index(color+'K'))
            break

    new_board = make_move(board, move)
    if not kings_location:
        for row in new_board:
            print(row)
    if under_attack(kings_location[0], kings_location[1], color, new_board):
        return True
    return False

#Checks for checks and checkmate moves
def checks_and_checkmate(color, board, move):
    if is_check_move(color, board, move):
        move.is_check = True
        if is_checkmate_move(color, board, move):
            move.is_checkmate = True
    elif is_checkmate_move(color, board, move):
        move.is_stalemate = True

    return move

#Checks for moves resulting in opposing king being in check
def is_check_move(color, board, move):
    opp_color = 'b' if color == 'w' else 'w'
    for r, row in enumerate(board):
        if opp_color + 'K' in row:
            kings_location = (r, row.index(opp_color+'K'))
            break

    new_board = make_move(board, move)
    if under_attack(kings_location[0], kings_location[1], opp_color, new_board):
        return True
    return False

#Checks for moves resulting in checkmate or stalemate
def is_checkmate_move(color, board, move):
    opp_color = 'b' if color == 'w' else 'w'
    new_board = make_move(board, move)
    moves = get_board_moves(new_board, opp_color, False)

    if moves:
        return False
    return True
