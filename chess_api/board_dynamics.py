from . import models
import copy

# Takes a board and a move and then returns a board after making the move
def make_move(board, move):
    new_board = copy.deepcopy(board)
    piece_moved = board[move.start[0]][move.start[1]]
    new_board[move.start[0]][move.start[1]] = '--'
    new_board[move.end[0]][move.end[1]] = piece_moved[0] + piece_moved[1]
    if piece_moved[1] == 'P' and abs(move.end[0] - move.start[0]) == 2:
        if move.end[1] < 7 and board[move.end[0]][move.end[1] + 1][1] == 'P' and board[move.end[0]][move.end[1] + 1][0] != piece_moved[0]:
            new_board[move.end[0]][move.end[1] + 1] = board[move.end[0]][move.end[1] + 1] + 'e-'
        if move.end[1] > 0 and board[move.end[0]][move.end[1] - 1][1] == 'P' and board[move.end[0]][move.end[1] - 1][0] != piece_moved[0]:
            new_board[move.end[0]][move.end[1] - 1] = board[move.end[0]][move.end[1] - 1] + 'e+'

    for r, row in enumerate(new_board):
        for c, col in enumerate(new_board):
            if 'e' in col:
                new_board[r][c] = new_board[r][c][:2]
    
    return new_board

# Takes a board and a move and then returns a board after undoing the move
def undo_move(move):
    return move.board