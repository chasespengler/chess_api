import unittest
import sys
sys.path.append('..')
from chess_api import models, utils

class chessNotationTests(unittest.TestCase):

    #Test info for pawn moves

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

    #Test info for castling moves

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

if __name__ == '__main__':
    unittest.main()