# Chess bots
import random
from .board_dynamics import make_move, undo_move

def get_bot_move(num):
    bots = [get_level_1_move, get_level_1_move, get_level_2_move]
    return bots[num]

#Level 1 bot
def get_level_1_move(moves, board):
    return moves[random.randint(0, len(moves)-1)]

#Level 2 bot
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