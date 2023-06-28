import random
import logic
from logic import *

boards = []
recursive_pos = [fen_to_array("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")]


def find_valid_board_states(cur_pos=[], turn=''):
    # finds potential boards from current position

    castling_flags = [logic.white_k_castle, logic.white_q_castle, logic.black_k_castle, logic.black_q_castle]

    if not turn:
        turn = board.colorTurn
    if not cur_pos:
        cur_pos = board.current_position
    potential_boards = valid_boards(cur_pos, turn)
    valid_board_list = []
    print("Color turn: " + turn)

    # add in 4 castling boards from current position
    # castling flags: [whiteShortCastle, whiteLongCastle, blackShortCastle, blackLongCastle]

    if turn == 'w':
        castling_piece = 'K'
    else:
        castling_piece = 'k'

    # Creates boards for the four castling positions and tests if you can castle, if so add to potential boards
    if castling_flags[0] and turn == 'w':
        temp_board = copy.deepcopy(cur_pos)
        temp_board[7][7] = 'K'
        temp_board[7][4] = '0'
        if is_castling(cur_pos, temp_board, castling_piece, [7, 7], False):
            potential_boards.append(temp_board)
    if castling_flags[1] and turn == 'w':
        temp_board = copy.deepcopy(cur_pos)
        temp_board[7][0] = 'K'
        temp_board[7][4] = '0'
        if is_castling(cur_pos, temp_board, castling_piece, [7, 0], False):
            potential_boards.append(temp_board)
    if castling_flags[2] and turn == 'b':
        temp_board = copy.deepcopy(cur_pos)
        temp_board[0][7] = 'k'
        temp_board[0][4] = '0'
        if is_castling(cur_pos, temp_board, castling_piece, [0, 7], False):
            potential_boards.append(temp_board)
    if castling_flags[3] and turn == 'b':
        temp_board = copy.deepcopy(cur_pos)
        temp_board[0][0] = 'k'
        temp_board[0][4] = '0'
        if is_castling(cur_pos, temp_board, castling_piece, [0, 0], False):
            potential_boards.append(temp_board)

    for potential_board in potential_boards:
        valid_move = is_valid_move(cur_pos, potential_board, turn, False, False)
        if valid_move:
            valid_board_list.append(potential_board)

    print("# of valid moves:", len(valid_board_list))

    return valid_board_list


def random_engine():
    potential_boards = find_valid_board_states()

    return random.choice(potential_boards)


def greedy_engine():
    potential_boards = find_valid_board_states()
    max_eval = [100000, 0]

    for potential_board in potential_boards:
        eval = greedy_evaluation(potential_board)
        if eval <= max_eval[0]:
            max_eval[0] = eval
            max_eval[1] = potential_board

    return max_eval[1]


def greedy_evaluation(board_array):
    eval_score = 0
    for i in range(0,8):
        for j in range(0, 8):
            piece = board_array[i][j]
            if piece == 'p':
                eval_score -= 10
            elif piece == 'P':
                eval_score += 10
            elif piece == 'n':
                eval_score -= 30
            elif piece == 'N':
                eval_score += 30
            elif piece == 'b':
                eval_score -= 30
            elif piece == 'B':
                eval_score += 30
            elif piece == 'r':
                eval_score -= 50
            elif piece == 'R':
                eval_score += 50
            elif piece == 'q':
                eval_score -= 90
            elif piece == 'Q':
                eval_score += 90

    return eval_score


# def find_valid_board_states_recursive(depth, start=recursive_pos):
#     if depth == 0:
#         return boards
#
#     for position in find_valid_board_states([True, True, True, True], ):
#         boards.append(position)
#
#     depth -= 1
#
#     print("depth:", depth, "# of combinations:", len(boards))
#
#     find_valid_board_states_recursive(depth)


def main():
    # find_valid_board_states_recursive(2)
    pass


if __name__ == '__main__':
    main()
