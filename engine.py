import random
import logic
import math
from logic import *

boards = []
recursive_pos = [fen_to_array("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")]

# define engine constants
MAX_DEPTH = 3

# flag for state of the game
isEndgame = False


# store some preset values based on the position of the pawn
pawn_table = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [50, 50, 50, 50, 50, 50, 50, 50],
    [10, 10, 20, 30, 30, 20, 10, 10],
    [5, 5, 10, 25, 25, 10, 5, 5],
    [0, 0, 0, 20, 20, 0, 0, 0],
    [5, -5, -10, 0, 0, -10, -5, 5],
    [5, 10, 10, -20, -20, 10, 10, 5],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

pawn_table.reverse()

knight_table = [
    [-50, -40, -30, -30, -30, -30, -40, -50],
    [-40, -20, 0, 5, 5, 0, -20, -40],
    [-30, 5, 10, 15, 15, 10, 5, -30],
    [-30, 0, 15, 20, 20, 15, 0, -30],
    [-30, 5, 15, 20, 20, 15, 5, -30],
    [-30, 0, 10, 15, 15, 10, 0, -30],
    [-40, -20, 0, 0, 0, 0, -20, -40],
    [-50, -40, -30, -30, -30, -30, -40, -50]
]

knight_table.reverse()

bishop_table = [
    [-20, -10, -10, -10, -10, -10, -10, -20],
    [-10, 0, 0, 0, 0, 0, 0, -10],
    [-10, 0, 5, 10, 10, 5, 0, -10],
    [-10, 5, 5, 10, 10, 5, 5, -10],
    [-10, 0, 10, 10, 10, 10, 0, -10],
    [-10, 10, 10, 10, 10, 10, 10, -10],
    [-10, 5, 0, 0, 0, 0, 5, -10],
    [-20, -10, -10, -10, -10, -10, -10, -20]
]

bishop_table.reverse()

rook_table = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [5, 10, 10, 10, 10, 10, 10, 5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [0, 0, 0, 5, 5, 0, 0, 0]
]

rook_table.reverse()

queen_table = [
    [-20, -10, -10, -5, -5, -10, -10, -20],
    [-10, 0, 0, 0, 0, 5, 0, -10],
    [-10, 0, 5, 5, 5, 5, 5, -10],
    [-5, 0, 5, 5, 5, 5, 0, 0],
    [-5, 0, 5, 5, 5, 5, 0, -5],
    [-10, 0, 5, 5, 5, 5, 0, -10],
    [-10, 0, 0, 0, 0, 0, 0, -10],
    [-20, -10, -10, -5, -5, -10, -10, -20]
]

queen_table.reverse() 

king_table = [
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-20, -30, -30, -40, -40, -30, -30, 20],
    [-10, -20, -20, -20, -20, -20, -20, -10],
    [20, 20, 0, 0, 0, 0, 20, 20],
    [20, 30, 10, 0, 0, 10, 30, 20]
]

king_table.reverse()

king_end_game_table = [
    [-50, -40, -30, -20, -20, -30, -40, -50],
    [-30, -20, -10, 0, 0, -10, -20, -30],
    [-30, -10, 20, 30, 30, 20, -10, -30],
    [-30, -10, 30, 40, 40, 30, -10, -30],
    [-30, -10, 30, 40, 40, 30, -10, -30],
    [-30, -10, 20, 30, 30, 20, -10, -30],
    [-30, -30, 0, 0, 0, 0, -30, -30],
    [-50, -30, -30, -30, -30, -30, -30, 50]
]

king_end_game_table.reverse()

def evaluate_board(board_array, turnColor):
    piece_values = {
        'P': -100, 'N': -320, 'B': -330, 'R': -500, 'Q': -900, 'K': -20000,
        'p': 100, 'n': 320, 'b': 330, 'r': 500, 'q': 900, 'k': 20000
    }
    
    mobility_score = 0
    pawn_structure_score = 0
    king_safety_score = 0

    score = 0
    for i in range(8):
        for j in range(8):
            piece = board_array[i][j]
            if piece in piece_values:
                score += piece_values[piece]
                
                # calculate mobility score
                valid_moves = find_valid_moves(board_array, (i, j))
                mobility_score += len(valid_moves)

                # calculate pawn structure score
                if piece.lower() == 'p':
                    if board_array[i-1][j] == piece or board_array[i+1][j] == piece: # if there is a pawn on an adjacent file
                        pawn_structure_score += 10 # connected pawns
                    if j > 0 and board_array[i][j-1] != piece and j < 7 and board_array[i][j+1] != piece: # if there is no pawn on both sides
                        pawn_structure_score -= 20 # isolated pawn
                
                # calculate king safety score
                if piece.lower() == 'k':
                    if i in [0, 7] or j in [0, 7]: # if the king is on the edge
                        king_safety_score -= 50
                        
                # add position score from piece square table
                if piece.lower() == 'p':
                    score += pawn_table[i][j] if piece.isupper() else -pawn_table[7-i][7-j]  # White pawns want to advance, black pawns want to go down
                elif piece.lower() == 'n':
                    score += knight_table[i][j] if piece.isupper() else -knight_table[7-i][7-j]
                elif piece.lower() == 'b':
                    score += bishop_table[i][j] if piece.isupper() else -bishop_table[7-i][7-j]
                elif piece.lower() == 'r':
                    score += rook_table[i][j] if piece.isupper() else -rook_table[7-i][7-j]
                elif piece.lower() == 'q':
                    score += queen_table[i][j] if piece.isupper() else -queen_table[7-i][7-j]
                elif piece.lower() == 'k':
                    score += king_table[i][j] if piece.isupper() else -king_table[7-i][7-j]


    normalized_score = (score + mobility_score + pawn_structure_score + king_safety_score) / 100

    return normalized_score


def minimax(board_array, depth, alpha, beta, is_maximizing, turnColor):
    if not board_array:
        return

    if depth == 0:
        return evaluate_board(board_array, turnColor), board_array

    if is_maximizing:
        max_eval = float('-inf')
        best_board = None
        for next_board in find_valid_board_states(board_array, turnColor):
            eval_board, _ = minimax(next_board, depth - 1, alpha, beta, not is_maximizing, turnColor)
            if eval_board > max_eval:
                max_eval = eval_board
                best_board = next_board
            alpha = max(alpha, eval_board)
            if beta <= alpha:
                break
        return max_eval, best_board
    else:
        min_eval = float('inf')
        best_board = None
        opposite_color = 'w' if turnColor == 'b' else 'b'
        for next_board in find_valid_board_states(board_array, opposite_color):
            eval_board, _ = minimax(next_board, depth - 1, alpha, beta, not is_maximizing, turnColor)
            if eval_board < min_eval:
                min_eval = eval_board
                best_board = next_board
            beta = min(beta, eval_board)
            if beta <= alpha:
                break
        return min_eval, best_board

    
# def find_best_move(board_array, turnColor):
#     max_eval = float('-inf')
#     best_board = None

#     valid_board_list = find_valid_board_states(board_array, turnColor)

#     for next_board in valid_board_list:
#         eval_board = minimax(next_board, 3, -math.inf, math.inf, True, 'b')
#         if eval_board > max_eval:
#             max_eval = eval_board
#             best_board = next_board

#     return best_board



def find_valid_board_states(cur_pos=[], turn=''):
    # finds potential boards from current position

    castling_flags = [logic.white_k_castle, logic.white_q_castle, logic.black_k_castle, logic.black_q_castle]

    if not turn:
        turn = board.colorTurn
    if not cur_pos:
        cur_pos = board.current_position
    potential_boards = valid_boards(cur_pos, turn)
    valid_board_list = []

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
            # If valid, next check to see if a pawn needs promotion (only checking black for engine)
            promote_coord = promote(potential_board)
            if promote_coord != []:
                potential_board[promote_coord[0]][promote_coord[1]] = 'q'
            valid_board_list.append(potential_board)
    
    # eval = minimax(board.current_position, 3, float('-inf'), float('inf'), True, board.colorTurn)

    # print(f"eval: {eval}, # of valid moves: {len(valid_board_list)}")

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
