# Chess bots
import random

def get_bot_move(num):
    bots = [get_level_1_move, get_level_1_move]
    return bots[num]

#Level 1 bot
def get_level_1_move(moves, board):
    return moves[random.randint(0, len(moves)-1)]