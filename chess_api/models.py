
class move():
    def __init__(self, start, end, end_piece, board, is_castle=False, castle_type='', is_en_passant=False):
        self.start = start
        self.end = end
        self.end_piece = end_piece
        self.board = board
        self.is_castle = is_castle
        self.castle_type = castle_type
        self.is_en_passant = is_en_passant