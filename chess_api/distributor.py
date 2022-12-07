from . import board_dynamics, piece_moves, models, bots
from .utils import chess_notation
from flask import Blueprint, jsonify, request
from flask_required_args import required_data

bp = Blueprint('chess_api', __name__)

@bp.route('/get-move', methods=['GET'])
def get_move():
    r_board = request.args.get('board')
    board=[]
    colors_turn = request.args.get('colors_turn')
    castleability = request.args.get('castleability').split(',')
    bot_level = int(request.args.get('bot_level'))
    r_board = r_board.split(',')
    for row in r_board:
        board.append(row.split('.'))

    bot = bots.get_bot_move(bot_level)
    moves = piece_moves.get_board_moves(board, colors_turn[0])
    new_moves = piece_moves.add_castles(colors_turn, castleability, board)
    if new_moves:
        moves.extend(new_moves)

    move = bot(moves, board)
    algebraic_notation_move = chess_notation(move)

    return jsonify(success=True, board=board, move=algebraic_notation_move)
