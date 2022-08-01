from logic import *
from board import current_position, colorTurn

def find_valid_board_states(castling_flags):
    # finds potential boards from current position
    potential_boards = valid_boards(board.current_position, board.colorTurn)
    print("Color turn:" + board.colorTurn)

    # add in 4 castling boards from current position
    # castling flags: [whiteShortCastle, whiteLongCastle, blackShortCastle, blackLongCastle]

    for potential_board in potential_boards:
        valid_move = is_valid_move(board.current_position, potential_board, board.colorTurn, False)

        if not valid_move:
            potential_boards.remove(potential_board)

    print(len(potential_boards))

    return potential_boards
