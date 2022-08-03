from logic import *
from board import current_position, colorTurn


def find_valid_board_states(castling_flags):
    # finds potential boards from current position
    potential_boards = valid_boards(board.current_position, board.colorTurn)
    valid_board_list = []

    # add in 4 castling boards from current position
    # castling flags: [whiteShortCastle, whiteLongCastle, blackShortCastle, blackLongCastle]

    # if castling_flags[0]:
    #     temp_board = copy.deepcopy(board.current_position)
    #     potential_boards.append(temp_board)

    for potential_board in potential_boards:
        valid_move = is_valid_move(board.current_position, potential_board, board.colorTurn, False)
        if valid_move:
            valid_board_list.append(potential_board)

    print("# of valid moves:", len(valid_board_list))

    return valid_board_list
