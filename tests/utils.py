import unittest
from chess_api import models, utils

class chessNotationTests(unittest.TestCase):

    start_board = [  
['wR', 'wN', 'wB', 'wK', 'wQ', 'wB', 'wN', 'wR'],  
['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],  
['--', '--', '--', '--', '--', '--', '--', '--'],  
['--', '--', '--', '--', '--', '--', '--', '--'],  
['--', '--', '--', '--', '--', '--', '--', '--'],  
['--', '--', '--', '--', '--', '--', '--', '--'],  
['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],  
['bR', 'bN', 'bB', 'bK', 'bQ', 'bB', 'bN', 'bR']  
]  

    pawn_move = models.move((1, 0), (3, 0), '--', start_board)

    def test_standard(self, pawn_move):
        self.assertEqual(utils.chess_notation(pawn_move), 'a3')

if __name__ == '__main__':
    unittest.main()