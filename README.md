# Chess API
Takes the gamestate of a chess match in the following format:

{'board': [],
'colors_turn': 'white',
'castleability': [],
'bot_level': 3}

and returns a move.

#### Board format
##### Starting format
[
['wR', 'wN', 'wB', 'wK', 'wQ', 'wB', 'wN', 'wR],
['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
['--', '--', '--', '--', '--', '--', '--', '--'],
['--', '--', '--', '--', '--', '--', '--', '--'],
['--', '--', '--', '--', '--', '--', '--', '--'],
['--', '--', '--', '--', '--', '--', '--', '--'],
['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
['bR', 'bN', 'bB', 'bK', 'bQ', 'bB', 'bN', 'bR]
]
##### En Passant flag
If a pawn has the ability to capture via en passant, append an 'e' to the end of the piece's string followed by the direction
[
['wR', 'wN', 'wB', 'wK', 'wQ', 'wB', 'wN', 'wR],
['wP', 'wP', 'wP', '--', 'wP', 'wP', 'wP', 'wP'],
['--', '--', '--', '--', '--', '--', '--', '--'],
['--', '--', '--', '--', '--', '--', '--', '--'],
['--', '--', '--', 'wPe+', 'bP', '--', '--', '--'],
['--', 'bP', '--', '--', '--', '--', '--', '--'],
['bP', '--', 'bP', 'bP', '--', 'bP', 'bP', 'bP'],
['bR', 'bN', 'bB', 'bK', 'bQ', 'bB', 'bN', 'bR]
]



#### Castleability format
['wQs', 'wKs', 'bQs', 'bKs']

where each symbol corresponds with the color and Queenside or Kingside ability to castle.

#### Bot Levels
1-4