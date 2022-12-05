from . import board_dynamics, piece_moves, models, bots
from flask import Blueprint, jsonify, request

bp = Blueprint('chess_api', __name__)

@bp.route('/get-move', methods=['GET'])
def get_move():
    r_board = request.args.get('board')
    board=[]
    colors_turn = request.form.get('colors_turn')
    castleability = request.form.get('castleability')
    bot_level = request.form.get('bot_level')
    print('*'*100)
    print(r_board)
    print(type(r_board))
    r_board = r_board.split(',')
    for row in r_board:
        print(row.split('.'))
        board.append(row.split('.'))
    print(board)
    print('*'*100)

    #bot = bots.get_bot_move(bot_level)
    moves = []

    # for r, row in enumerate(board):
    #     for c, piece in enumerate(row):
    #         if piece[0] == colors_turn:
    #             moves.append(piece_moves.get_moves(r, c, board))

    return jsonify(success=True, board=board)
