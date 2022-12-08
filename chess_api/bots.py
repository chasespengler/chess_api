# Chess bots
import random
from .board_dynamics import make_move, undo_move
from .piece_moves import under_attack, get_board_moves, add_castles

#Scores current board
def calc_score(board):
    score = 0
    points = {'P': 1, 'R': 5, 'N': 3, 'B': 3, 'Q': 9, '-': 0}
    for row in board:
        for key, val in points.items():
            score += row.count('w'+key) * val
            score -= row.count('b'+key) * val

    return score


def get_bot_move(num):
    bots = [get_level_1_move, get_level_1_move, get_level_2_move, get_level_3_move, get_level_4_move, get_level_5_move]
    return bots[num]

#Level 1 bot
def get_level_1_move(moves, board, castleability):
    return moves[random.randint(0, len(moves)-1)]

#Level 2 bot, maximizes point differential after a move
def get_level_2_move(moves, board, castleability):
    points = {'P': 1, 'R': 5, 'N': 3, 'B': 3, 'Q': 9}
    max_take = 0
    opt_move = moves[random.randint(0, len(moves)-1)]
    for move in moves:
        if move.is_checkmate:
            return move
        if move.is_promotion:
            max_take = 9
            opt_move = move
        piece_taken = move.end_piece
        if piece_taken == '--':
            continue
        else:
            if points[piece_taken[1]] > max_take:
                max_take = points[piece_taken[1]]
                opt_move = move

    return opt_move

#Level 3 bot, minimizing maximum outcome of opponent's next move
def get_level_3_move(moves, board, castleability):
    color = board[moves[0].start[0]][moves[0].start[1]][0]
    opp_color = 'b' if color == 'w' else 'w'
    points = {'P': 1, 'R': 5, 'N': 3, 'B': 3, 'Q': 9, '-': 0}
    min_max = 100
    for move in moves:
        if move.is_checkmate:
            return move
        elif move.is_stalemate:
            continue
        maximum = 0
        points_for = -points[move.end_piece[1]]
        new_board = make_move(board, move)
        opp_moves = get_board_moves(new_board, opp_color)
        opp_moves.extend(add_castles(opp_color, castleability, board))
        for opp_move in opp_moves:
            if opp_move.is_checkmate:
                maximum = 100
            points_against = points[opp_move.end_piece[1]]
            if points_against > maximum:
                maximum = points_against

        if maximum + points_for < min_max:
            opt_move = move
            min_max = maximum

    return opt_move

#Level 4 bot, min max at increased depth
def get_level_4_move(moves, board, castleability):
    global opt_move
    opt_move = None
    random.shuffle(moves)
    color = board[moves[0].start[0]][moves[0].start[1]][0]
    alpha = -100
    beta = 100
    turn_coef = 1 if color == 'w' else -1
    min_max(moves, board, castleability, 2, 2, turn_coef)
    return opt_move

#Level 5
def get_level_5_move(moves, board, castleability):
    pass


def min_max(moves, board, castleability, depth, max_depth, turn_coef):
    global opt_move
    if depth == 0:
        return turn_coef * calc_score(board)

    max_score = -300
    for move in moves:
        new_board = make_move(board, move)
        new_moves = get_board_moves(new_board, 'w' if turn_coef > 0 else 'b', True)
        score = -min_max(new_moves, new_board, castleability, depth - 1, max_depth, -turn_coef)
        if score > max_score:
            max_score = score
            if depth == max_depth:
                opt_move = move

    return max_score