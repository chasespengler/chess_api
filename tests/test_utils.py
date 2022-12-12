import unittest
import sys
sys.path.append('..')
from chess_api import models, utils

class chessNotationTests(unittest.TestCase):

    #########################
    #Test info for pawn moves
    #########################

    pawns_board = [  
    ['wR', 'wN', 'wB', 'wK', 'wQ', 'wB', 'wN', '--'],  
    ['wP', 'wP', '--', 'wP', '--', 'wP', 'wP', 'bP'],  
    ['--', '--', 'bP', '--', 'bP', 'bP', '--', '--'],  
    ['--', '--', '--', '--', 'wP', '--', '--', '--'],  
    ['--', '--', '--', 'bP', '--', '--', 'bP', 'wPe-'],  
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['bP', 'bP', 'wP', '--', 'bP', 'bP', '--', 'bP'],  
    ['--', '--', '--', '--', '--', '--', '--', '--']  
    ]  

    pawn_move_1 = models.move((1, 0), (3, 0), '--', pawns_board)
    pawn_move_2 = models.move((1, 0), (2, 0), '--', pawns_board)
    pawn_move_3 = models.move((3, 4), (4, 3), 'bP', pawns_board)
    pawn_move_4 = models.move((4, 3), (3, 4), 'wP', pawns_board)
    pawn_move_5 = models.move((4, 7), (5, 6), '--', pawns_board, is_en_passant=True)
    pawn_move_6 = models.move((2, 2), (1, 2), '--', pawns_board, is_check=True)
    pawn_move_7 = models.move((6, 2), (7, 2), '--', pawns_board, is_promotion=True)
    pawn_move_8 = models.move((6, 2), (7, 2), '--', pawns_board, is_promotion=True, piece_promoted='B')
    pawn_move_9 = models.move((2, 4), (1, 4), '--', pawns_board, is_check=True, is_checkmate=True)
    pawn_move_10 = models.move((1, 7), (0, 7), '--', pawns_board, is_promotion=True)
    pawn_move_11 = models.move((1, 7), (0, 7), '--', pawns_board, is_promotion=True, piece_promoted='N')

    def test_pawns(self):
        #Opening move white
        self.assertEqual(utils.chess_notation(self.pawn_move_1), 'h4')
        #Regular move white
        self.assertEqual(utils.chess_notation(self.pawn_move_2), 'h3')
        #Capturing another pawn white
        self.assertEqual(utils.chess_notation(self.pawn_move_3), 'dxe5')
        #Capturing another pawn black
        self.assertEqual(utils.chess_notation(self.pawn_move_4), 'exd4')
        #Capturing another pawn white via en passant to the left (right from white's perspective)
        self.assertEqual(utils.chess_notation(self.pawn_move_5), 'axb6 e.p.')
        #Check move straight black
        self.assertEqual(utils.chess_notation(self.pawn_move_6), 'f2+')
        #Default pawn promotion white
        self.assertEqual(utils.chess_notation(self.pawn_move_7), 'f8=Q')
        #Chosen pawn promotion white
        self.assertEqual(utils.chess_notation(self.pawn_move_8), 'f8=B')
        #Checkmate pawn move black
        self.assertEqual(utils.chess_notation(self.pawn_move_9), 'd2++')
        #Default pawn promotion black
        self.assertEqual(utils.chess_notation(self.pawn_move_10), 'a1=Q')
        #Chosen pawn promotion black
        self.assertEqual(utils.chess_notation(self.pawn_move_11), 'a1=N')
        #Check move via capture
        #Check move via capture via en passant

    #############################
    #Test info for castling moves
    #############################

    castles_board = [  
    ['wR', '--', '--', 'wK', '--', '--', '--', 'wR'],  
    ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],  
    ['--', '--', '--', '--', '--', '--', '--', '--'],  
    ['--', '--', '--', '--', '--', '--', '--', '--'],  
    ['--', '--', '--', '--', '--', '--', '--', '--'],  
    ['--', '--', '--', '--', '--', '--', '--', '--'], 
    ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],  
    ['bR', '--', '--', 'bK', '--', '--', '--', 'bR']  
    ]  

    castle_move_1 = models.move((7, 3), (7, 0), '--', castles_board, is_castle=True, castle_type='bKs')
    castle_move_2 = models.move((7, 3), (7, 7), '--', castles_board, is_castle=True, castle_type='bQs')
    castle_move_3 = models.move((0, 3), (0, 0), '--', castles_board, is_castle=True, castle_type='wKs')
    castle_move_4 = models.move((0, 3), (0, 7), '--', castles_board, is_castle=True, castle_type='wQs')

    def test_castles(self):
        #Black kingside
        self.assertEqual(utils.chess_notation(self.castle_move_1), 'O-O')
        #Black queenside
        self.assertEqual(utils.chess_notation(self.castle_move_2), 'O-O-O')
        #White kingside
        self.assertEqual(utils.chess_notation(self.castle_move_3), 'O-O')
        #White queenside
        self.assertEqual(utils.chess_notation(self.castle_move_4), 'O-O-O')

    ##########################
    #Test info for kings moves
    ##########################

    kings_board = [  
    ['--', 'bR', 'bB', 'bR', '--', '--', '--', '--'],  
    ['--', 'bB', 'wK', 'bB', '--', '--', 'wK', '--'],  
    ['--', 'bR', 'bB', 'bR', '--', '--', '--', '--'],  
    ['--', '--', '--', '--', '--', '--', '--', '--'],  
    ['--', '--', '--', '--', '--', '--', '--', '--'],  
    ['--', 'wR', 'wB', 'wR', '--', '--', '--', '--'], 
    ['--', 'wB', 'bK', 'wB', '--', '--', 'bK', '--'],  
    ['--', 'wR', 'wB', 'wR', '--', '--', '--', '--'] 
    ]

    king_move_1w = models.move((1, 2), (0, 1), 'bR', kings_board)
    king_move_2w = models.move((1, 2), (0, 3), 'bR', kings_board)
    king_move_3w = models.move((1, 2), (2, 1), 'bR', kings_board)
    king_move_4w = models.move((1, 2), (2, 3), 'bR', kings_board)

    king_move_5w = models.move((1, 2), (0, 2), 'bB', kings_board)
    king_move_6w = models.move((1, 2), (1, 1), 'bB', kings_board)
    king_move_7w = models.move((1, 2), (1, 3), 'bB', kings_board)
    king_move_8w = models.move((1, 2), (2, 2), 'bB', kings_board)

    king_move_9w = models.move((1, 6), (0, 5), '--', kings_board)
    king_move_10w = models.move((1, 6), (0, 6), '--', kings_board)
    king_move_11w = models.move((1, 6), (0, 7), '--', kings_board)

    king_move_12w = models.move((1, 6), (1, 5), '--', kings_board)
    king_move_13w = models.move((1, 6), (1, 7), '--', kings_board)

    king_move_14w = models.move((1, 6), (2, 5), '--', kings_board)
    king_move_15w = models.move((1, 6), (2, 6), '--', kings_board)
    king_move_16w = models.move((1, 6), (2, 7), '--', kings_board)

    king_move_1b = models.move((6, 2), (5, 1), 'wR', kings_board)
    king_move_2b = models.move((6, 2), (5, 3), 'wR', kings_board)
    king_move_3b = models.move((6, 2), (7, 1), 'wR', kings_board)
    king_move_4b = models.move((6, 2), (7, 3), 'wR', kings_board)

    king_move_5b = models.move((6, 2), (5, 2), 'wB', kings_board)
    king_move_6b = models.move((6, 2), (6, 1), 'wB', kings_board)
    king_move_7b = models.move((6, 2), (6, 3), 'wB', kings_board)
    king_move_8b = models.move((6, 2), (7, 2), 'wB', kings_board)

    king_move_9b = models.move((6, 6), (5, 5), '--', kings_board)
    king_move_10b = models.move((6, 6), (5, 6), '--', kings_board)
    king_move_11b = models.move((6, 6), (5, 7), '--', kings_board)

    king_move_12b = models.move((6, 6), (6, 5), '--', kings_board)
    king_move_13b = models.move((6, 6), (6, 7), '--', kings_board)

    king_move_14b = models.move((6, 6), (7, 5), '--', kings_board)
    king_move_15b = models.move((6, 6), (7, 6), '--', kings_board)
    king_move_16b = models.move((6, 6), (7, 7), '--', kings_board)

    def test_kings(self):
        #White diagonal captures
        self.assertEqual(utils.chess_notation(self.king_move_1w), 'Kxg1')
        self.assertEqual(utils.chess_notation(self.king_move_2w), 'Kxe1')
        self.assertEqual(utils.chess_notation(self.king_move_3w), 'Kxg3')
        self.assertEqual(utils.chess_notation(self.king_move_4w), 'Kxe3')

        #White horizontal/vertical captures
        self.assertEqual(utils.chess_notation(self.king_move_5w), 'Kxf1')
        self.assertEqual(utils.chess_notation(self.king_move_6w), 'Kxg2')
        self.assertEqual(utils.chess_notation(self.king_move_7w), 'Kxe2')
        self.assertEqual(utils.chess_notation(self.king_move_8w), 'Kxf3')

        #White moves backwards
        self.assertEqual(utils.chess_notation(self.king_move_9w), 'Kc1')
        self.assertEqual(utils.chess_notation(self.king_move_10w), 'Kb1')
        self.assertEqual(utils.chess_notation(self.king_move_11w), 'Ka1')

        #White moves adjacent
        self.assertEqual(utils.chess_notation(self.king_move_12w), 'Kc2')
        self.assertEqual(utils.chess_notation(self.king_move_13w), 'Ka2')

        #White moves forward
        self.assertEqual(utils.chess_notation(self.king_move_14w), 'Kc3')
        self.assertEqual(utils.chess_notation(self.king_move_15w), 'Kb3')
        self.assertEqual(utils.chess_notation(self.king_move_16w), 'Ka3')

        #Black diagonal captures
        self.assertEqual(utils.chess_notation(self.king_move_1b), 'Kxg6')
        self.assertEqual(utils.chess_notation(self.king_move_2b), 'Kxe6')
        self.assertEqual(utils.chess_notation(self.king_move_3b), 'Kxg8')
        self.assertEqual(utils.chess_notation(self.king_move_4b), 'Kxe8')

        #Black horizontal/vertical captures
        self.assertEqual(utils.chess_notation(self.king_move_5b), 'Kxf6')
        self.assertEqual(utils.chess_notation(self.king_move_6b), 'Kxg7')
        self.assertEqual(utils.chess_notation(self.king_move_7b), 'Kxe7')
        self.assertEqual(utils.chess_notation(self.king_move_8b), 'Kxf8')

        #Black moves backwards
        self.assertEqual(utils.chess_notation(self.king_move_9b), 'Kc6')
        self.assertEqual(utils.chess_notation(self.king_move_10b), 'Kb6')
        self.assertEqual(utils.chess_notation(self.king_move_11b), 'Ka6')

        #Black moves adjacent
        self.assertEqual(utils.chess_notation(self.king_move_12b), 'Kc7')
        self.assertEqual(utils.chess_notation(self.king_move_13b), 'Ka7')

        #Black moves forward
        self.assertEqual(utils.chess_notation(self.king_move_14b), 'Kc8')
        self.assertEqual(utils.chess_notation(self.king_move_15b), 'Kb8')
        self.assertEqual(utils.chess_notation(self.king_move_16b), 'Ka8')



if __name__ == '__main__':
    unittest.main()