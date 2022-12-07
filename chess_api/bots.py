# Chess bots
import random
from .board_dynamics import make_move, undo_move
from .piece_moves import under_attack, get_board_moves

def get_bot_move(num):
    bots = [get_level_1_move, get_level_1_move, get_level_2_move, get_level_3_move]
    return bots[num]

#Level 1 bot
def get_level_1_move(moves, board):
    return moves[random.randint(0, len(moves)-1)]

#Level 2 bot, maximizes point differential after a move
def get_level_2_move(moves, board):
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
def get_level_3_move(moves, board):
    color = board[moves[0].start[0]][moves[0].start[1]][0]
    opp_color = 'b' if color == 'w' else 'w'
    points = {'P': 1, 'R': 5, 'N': 3, 'B': 3, 'Q': 9, '-': 0}
    min_max = 100
    for move in moves:
        if move.is_checkmate:
            return move
        maximum = 0
        points_for = -points[move.end_piece[1]]
        new_board = make_move(board, move)
        opp_moves = get_board_moves(new_board, opp_color)
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
