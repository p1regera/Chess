from logic import *
from board import current_position, colorTurn

def evaluate_board(board_array, turnColor):
    piece_values = {
        'P': 100, 'N': 320, 'B': 330, 'R': 500, 'Q': 900, 'K': 20000,
        'p': -100, 'n': -320, 'b': -330, 'r': -500, 'q': -900, 'k': -20000
    }

    score = 0
    for i in range(8):
        for j in range(8):
            piece = board_array[i][j]
            if piece in piece_values:
                score += piece_values[piece]

    normalized_score = score / 100

    return normalized_score

def minimax(board_array, depth, alpha, beta, is_maximizing, turnColor):
    if depth == 0:
        return evaluate_board(board_array, turnColor)

    if is_maximizing:
        max_eval = float('-inf')
        for next_board in valid_boards(board_array, turnColor):
            eval_board = minimax(next_board, depth - 1, alpha, beta, not is_maximizing, turnColor)
            max_eval = max(max_eval, eval_board)
            alpha = max(alpha, eval_board)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        opposite_color = 'w' if turnColor == 'b' else 'b'
        for next_board in valid_boards(board_array, opposite_color):
            eval_board = minimax(next_board, depth - 1, alpha, beta, not is_maximizing, turnColor)
            min_eval = min(min_eval, eval_board)
            beta = min(beta, eval_board)
            if beta <= alpha:
                break
        return min_eval


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

    
    eval = minimax(board.current_position, 3, float('-inf'), float('inf'), True, board.colorTurn)

    print(f"eval: {eval}, # of valid moves: {len(valid_board_list)}")

    return valid_board_list
