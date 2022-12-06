
class move():
    def __init__(self, start, end, end_piece, board, is_castle=False, castle_type='', is_en_passant=False, is_check=False, is_checkmate=False, is_promotion=False, piece_promoted='Q'):
        self.start = start
        self.end = end
        self.end_piece = end_piece
        self.board = board
        self.is_castle = is_castle
        self.castle_type = castle_type
        self.is_en_passant = is_en_passant
        self.is_check = is_check
        self.is_checkmate = is_checkmate
        self.is_promotion = is_promotion
        self.piece_promoted = piece_promoted

    def get_piece_moved(self):
        return self.board[self.start[0]][self.start[1]]