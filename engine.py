from logic import *
from board import current_position, colorTurn

boards = []


def find_valid_board_states(castling_flags=[True, True, True, True]):
    # finds potential boards from current position
    potential_boards = valid_boards(board.current_position, board.colorTurn)
    valid_board_list = []
    print("Color turn:" + board.colorTurn)

    # add in 4 castling boards from current position
    # castling flags: [whiteShortCastle, whiteLongCastle, blackShortCastle, blackLongCastle]

    if board.colorTurn == 'w':
        castling_piece = 'K'
    else:
        castling_piece = 'k'

    # Creates boards for the four castling positions and tests if you can castle, if so add to potential boards
    if castling_flags[0] and board.colorTurn == 'w':
        temp_board = copy.deepcopy(board.current_position)
        temp_board[7][7] = 'K'
        temp_board[7][4] = '0'
        if is_castling(board.current_position, temp_board, castling_piece, [7, 7], False):
            potential_boards.append(temp_board)
    if castling_flags[1] and board.colorTurn == 'w':
        temp_board = copy.deepcopy(board.current_position)
        temp_board[7][0] = 'K'
        temp_board[7][4] = '0'
        if is_castling(board.current_position, temp_board, castling_piece, [7, 0], False):
            potential_boards.append(temp_board)
    if castling_flags[2] and board.colorTurn == 'b':
        temp_board = copy.deepcopy(board.current_position)
        temp_board[0][7] = 'k'
        temp_board[0][4] = '0'
        if is_castling(board.current_position, temp_board, castling_piece, [0, 7], False):
            potential_boards.append(temp_board)
    if castling_flags[3] and board.colorTurn == 'b':
        temp_board = copy.deepcopy(board.current_position)
        temp_board[0][0] = 'k'
        temp_board[0][4] = '0'
        if is_castling(board.current_position, temp_board, castling_piece, [0, 0], False):
            potential_boards.append(temp_board)

    for potential_board in potential_boards:
        valid_move = is_valid_move(board.current_position, potential_board, board.colorTurn, False, False)
        if valid_move:
            valid_board_list.append(potential_board)

    print("# of valid moves:", len(valid_board_list))

    return valid_board_list


def find_valid_board_states_recursive(depth):
    if depth == 0:
        return boards

    for position in find_valid_board_states():
        boards.append(position)

    depth -= 1

    print("depth:", depth, "# of combinations:", len(boards))

    find_valid_board_states_recursive(depth)


def main():
    find_valid_board_states_recursive(4)


if __name__ == '__main__':
    main()
