# Take move object and returns move in chess notation
def chess_notation(move):
    piece = move.get_piece_moved()
    move_string = piece[1] if piece[1] != 'P' and not move.is_castle else ''
    move_string += need_clarification(move)
    if move.end_piece != '--':
        move_string += 'x'
    if not move_string.is_castle:
        cols = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
        move_string += cols[move.end[1]]
        move_string += move.end[0] + 1
    if move.is_castle:
        if move.castle_type[1] == 'K':
            move_string = 'O-O'
        else:
            move_string = 'O-O-O'
    if move.is_check:
        move_string += '+'
    if move.is_checkmate:
        move_string += '+'
    if move.is_en_passant:
        move_string += ' e.p.'
    elif move.is_promotion:
        move_string += '=' + move.piece_promoted

    return move_string

# Returns the character necessary if a move needs clarification e.g.
# knights on b1 and b3 can both move to d2 so the notation must be N1d2 or
# rooks on a1 and h8 can both move to d8 so the notation must be Rad8
def need_clarification(move):
    board =  move.board
    piece = move.get_piece_moved()
    end_position = move.end
    other_positions = []

    if piece[1] == 'N':
        vectors = [(1, 2), (2, 1), (-1, 2), (1, -2), (2, -1), (-2, 1), (-2, -1), (-1, -2)]
        for vector in vectors:
            row = vector[0] + end_position[0]
            col = vector[1] + end_position[1]
            if allowed(row, col):
                if board[row][col] == piece[:2] and ((row, col) != move.start):
                    other_positions.append((row, col))

    elif piece[1] == 'B' or piece[1] == 'Q':
        vectors = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        for vector in vectors:
            for i in range(1, 8):
                row = end_position[0] + i*vector[0]
                col = end_position[1] + i*vector[1]
                if allowed(row, col):
                    if board[row][col] == '--':
                        continue
                    elif board[row][col] == piece[:2] and ((row, col) != move.start):
                        other_positions.append((row, col))
                        break
                    else:
                        break

    if piece[1] == 'R' or piece[1] == 'Q':
        vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for vector in vectors:
            for i in range(1, 8):
                row = end_position[0] + i*vector[0]
                col = end_position[1] + i*vector[1]
                if allowed(row, col):
                    if board[row][col] == '--':
                        continue
                    elif board[row][col] == piece[:2] and ((row, col) != move.start):
                        other_positions.append((row, col))
                        break
                    else:
                        break
    
    elif piece[1] == 'P':
        if move.end[1] != move.start[1]:
            if move.end[1] > move.start[1]:
                row = move.start[0]
                col = move.start[1] + 2
                if allowed(row, col):
                    if board[row][col] == piece[:2]:
                        other_positions.append((row, col))
            if move.end[1]< move.start[1]:
                row = move.start[0]
                col = move.start[1] - 2
                if allowed(row, col):
                    if board[row][col] == piece[:2]:
                        other_positions.append((row, col))


    if other_positions:
        character = ''
        is_row = False
        is_col = False
        for position in other_positions:
            if position[0] == move.start[0]:
                is_col = True
            if position[1] == move.start[1]:
                is_row = True

        if is_row:
            character += move.start[0] + 1
        if is_col:
            cols = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
            character += cols[move.start[1]]
        return character
    return ''

def allowed(row, col):
    if row >= 8 or row < 0 or col >= 8 or col < 0:
        return False
    return True