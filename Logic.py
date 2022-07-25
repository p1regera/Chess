import re
import time
import copy
from piece_movement import *

white_q_castle = True
white_k_castle = True
black_q_castle = True
black_k_castle = True

def fen_to_array(fen):
    # Helper function, turns 'test' into ['t', 'e', 's', 't']
    def split(word):
        return [char for char in word]

    # Helper function, inserts a string within a string at the specified index
    def insert(source_str, insert_str, pos):
        return source_str[:pos] + insert_str + source_str[pos:]

    # Split the FEN by each rank
    board_array = fen.split("/")

    # Trim the extra information off the FEN
    first_rank = board_array[7]
    board_array[7] = first_rank[0:8]

    # Parse number for whitespaces into 0's in the right position
    for i in range(8):
        rank = board_array[i]
        for j in range(len(rank)):
            if re.match("[1-8]", rank[j]):
                board_array[i] = board_array[i].replace(rank[j], "0" * int(rank[j]), 1)

    # Use split function to turn into a 2d array
    for i in range(8):
        board_array[i] = split(board_array[i])

    return board_array


def is_valid_move(prev_board_array, cur_board_array, turnColor):
    if prev_board_array == cur_board_array:
        return False
    # Find which piece moves, and the starting and end position
    prev_pos = [10, 10]
    cur_pos = [10, 10]

    # Find the piece's start position
    for i in range(0, 8):
        for j in range(0, 8):
            # If this current spot on the board is 0 and last move it was not 0, this is where the piece moved from
            if cur_board_array[i][j] == "0" and prev_board_array[i][j] != "0":
                prev_pos = [i, j]
                # print("prev: ", prev_pos)
                piece = prev_board_array[i][j]

    # If it's not your turn, then the move is invalid
    if (piece.islower() and turnColor == 'w') or (piece.isupper() and turnColor == 'b'):
        return False

    # Find the piece's end position
    for i in range(0, 8):
        for j in range(0, 8):
            # If last move this spot was 0 or the opposite color, and now it is not 0 and not the opposite color,
            # this is where the piece currently lies
            if ((prev_board_array[i][j] == "0" or is_opposite_color(prev_board_array[i][j], piece)) and
                    (cur_board_array[i][j] != "0" and not is_opposite_color(cur_board_array[i][j], piece))):
                cur_pos = [i, j]
                # print("cur: ", cur_pos)

    # If the piece moved to a valid position (based on what type of piece), then return true
    if cur_pos not in find_valid_moves(prev_board_array, prev_pos):
        return False

    # Update castling parameters
    castle_update(piece, prev_pos)

    # If the player moving the piece is in check after the move, the move is invalid
    check = is_in_check(cur_board_array, turnColor)

    if check == "Both" and turnColor == 'b':
        return False
    if check == "White" and turnColor == 'w':
        return False
    if check == "Black" and turnColor == 'b':
        return False
    if check == "White Checkmated":
        return "White Checkmated"
    if check == "Black Checkmated":
        return "Black Checkmated"

    return True


def find_valid_moves(board_array, piece_pos):
    # returns 2d list of all valid moves a piece can make i.e. [[x,y], [x,y], ..]
    piece = board_array[piece_pos[0]][piece_pos[1]]

    if piece in ['P', 'p']:
        return pawn_moves(board_array, piece_pos)
    elif piece in ['R', 'r']:
        return rook_moves(board_array, piece_pos)
    elif piece in ['N', 'n']:
        return knight_moves(board_array, piece_pos)
    elif piece in ['B', 'b']:
        return bishop_moves(board_array, piece_pos)
    elif piece in ['Q', 'q']:
        return queen_moves(board_array, piece_pos)
    elif piece in ['K', 'k']:
        return king_moves(board_array, piece_pos)
    else:
        return []


def is_in_check(board_array, turnColor):
    # Returns White/Black/Both/None depending on which king(s) are in check
    # Find the kings
    white_king_pos = []
    white_valid_moves = []
    black_king_pos = []
    black_valid_moves = []
    for i in range(0, 8):
        for j in range(0, 8):
            cur_piece = board_array[i][j]
            if cur_piece == 'K':
                white_king_pos = [i, j]
            elif cur_piece == 'k':
                black_king_pos = [i, j]
            elif cur_piece.isupper():
                for coord in find_valid_moves(board_array, [i, j]):
                    white_valid_moves.append(coord)
            else:
                for coord in find_valid_moves(board_array, [i, j]):
                    black_valid_moves.append(coord)

    white_checked = False
    black_checked = False

    if white_king_pos in black_valid_moves:
        white_checked = True
    if black_king_pos in white_valid_moves:
        black_checked = True

    if white_checked and black_checked:
        return "Both"

    if white_checked:
        if turnColor == 'b':
            checkmate = True
            for board in valid_boards(board_array, 'w'):
                if is_in_check(board, 'w') in ["Black", "Neither"]:
                    print('\n'.join(' '.join(str(x) for x in row) for row in board))
                    print(is_in_check(board, 'w'))
                    print("=================")
                    checkmate = False
                    break
            if checkmate:
                return "White Checkmated"
        return "White"

    if black_checked:
        if black_checked:
            if turnColor == 'w':
                checkmate = True
                for board in valid_boards(board_array, 'b'):
                    if is_in_check(board, 'b') in ["White", "Neither"]:
                        # Debugging purposes
                        print('\n'.join(' '.join(str(x) for x in row) for row in board))
                        print(is_in_check(board, 'b'))
                        print("=================")
                        checkmate = False
                        break
                if checkmate:
                    return "Black Checkmated"
        return "Black"
    else:
        return "Neither"


def valid_boards(board_array, turnColor):
    valid_board_list = []
    for i in range(0, 8):
        for j in range(0, 8):
            piece = board_array[i][j]
            if piece.isupper() and turnColor == 'w':
                valid_moves = find_valid_moves(board_array, [i, j])
                for move in valid_moves:
                    board_copy = copy.deepcopy(board_array)
                    board_copy[i][j] = '0'
                    board_copy[move[0]][move[1]] = piece
                    valid_board_list.append(board_copy)
            elif piece.islower() and turnColor == 'b':
                valid_moves = find_valid_moves(board_array, [i, j])
                if piece == 'r':
                    print(valid_moves)
                for move in valid_moves:
                    board_copy = copy.deepcopy(board_array)
                    board_copy[i][j] = '0'
                    board_copy[move[0]][move[1]] = piece
                    valid_board_list.append(board_copy)

    return valid_board_list


def is_castling(board_array, piece, cur_pos):
    # Returns "WQ" / "WK" / "BQ" / "BK" / False for the type of castling being attempted
    global white_q_castle
    global white_k_castle
    global black_q_castle
    global black_k_castle

    if piece == 'K':
        if cur_pos == [7, 0] and white_q_castle:
            if board_array[7][1] == '0' and board_array[7][2] == '0' and board_array[7][3] == '0':
                return "WQ"
        elif cur_pos == [7, 7] and white_k_castle:
            if board_array[7][5] == '0' and board_array[7][6] == '0':
                return "WK"
    elif piece == 'k':
        if cur_pos == [0, 0] and white_q_castle:
            if board_array[0][1] == '0' and board_array[0][2] == '0' and board_array[0][3] == '0':
                return "BQ"
        elif cur_pos == [0, 7] and white_k_castle:
            if board_array[0][5] == '0' and board_array[0][6] == '0':
                return "BK"

    return False


def castle_update(piece, prev_pos):
    global white_q_castle
    global white_k_castle
    global black_q_castle
    global black_k_castle
    if piece == 'K':
        white_q_castle = False
        white_k_castle = False
    elif piece == 'k':
        black_q_castle = False
        black_k_castle = False
    elif piece == 'R' and prev_pos == [7, 7]:
        white_k_castle = False
    elif piece == 'R' and prev_pos == [7, 0]:
        white_q_castle = False
    elif piece == 'r' and prev_pos == [0, 7]:
        black_k_castle = False
    elif piece == 'r' and prev_pos == [0, 0]:
        black_q_castle = False

    #print(white_q_castle)
    #print(white_k_castle)
    #print(black_q_castle)
    #print(black_k_castle)


def has_captured(previous_position, current_position):
    if len(previous_position) == 0:
        return False

    for i in range(8):
        for j in range(8):
            if current_position[i][j] != previous_position[-1][i][j] and current_position[i][j] != '0' and previous_position[-1][i][j] != '0':
                return True
    return False


def main():
    default = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    starting_pos = "rnbqkbnr/ppppp1pp/5p2/Q7/8/8/PPPPPPPP/RNB1KBNR w KQkq - 0 1"
    sec_pos = "rnb1k2r/ppppQppp/8/8/1B2P3/P2P2q1/P1P2PPP/RNB1KBNR w KQkq - 0 1"

    start = time.time()
    # print('\n'.join(' '.join(str(x) for x in row) for row in fen_to_array(starting_pos)))
    # print(find_valid_moves(fen_to_array(sec_pos), [3, 7]))
    # print(is_valid_move(fen_to_array(starting_pos), fen_to_array(sec_pos)))
    # print(rook_moves(fen_to_array(sec_pos), [0, 0]))
    # print('\n'.join(' '.join(str(x) for x in row) for row in fen_to_array(sec_pos)))
    # print(is_in_check(fen_to_array(sec_pos)), "is in check")
    end = time.time()
    # print(end - start)

    # print(is_in_check(fen_to_array(sec_pos), 'w'))


if __name__ == '__main__':
    main()