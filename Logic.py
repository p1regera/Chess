import re
import time
from piece_movement import *

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


def is_valid_move(prev_board_array, cur_board_array, colorTurn):
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
                print("prev: ", prev_pos)
                piece = prev_board_array[i][j]

    # If it's not your turn, then the move is invalid
    if (piece.islower() and colorTurn == 'w') or (piece.isupper() and colorTurn == 'b'):
        return False

    # Find the piece's end position
    for i in range(0, 8):
        for j in range(0, 8):
            # If last move this spot was 0 or the opposite color, and now it is not 0 and not the opposite color,
            # this is where the piece currently lies
            if ((prev_board_array[i][j] == "0" or is_opposite_color(prev_board_array[i][j], piece)) and
                    (cur_board_array[i][j] != "0" and not is_opposite_color(cur_board_array[i][j], piece))):
                cur_pos = [i, j]
                print("cur: ", cur_pos)

    # If the piece moved to a valid position (based on what type of piece), then return true
    if cur_pos not in find_valid_moves(prev_board_array, prev_pos):
        return False

    # If the player moving the piece is in check after the move, the move is invalid
    check = is_in_check(cur_board_array)

    if check == "Both" and colorTurn == 'b':
        return False
    if check == "White" and colorTurn == 'w':
        return False
    if check == "Black" and colorTurn == 'b':
        return False

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


def is_in_check(board_array):
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
    print(black_king_pos)
    print(white_valid_moves)

    if white_king_pos in black_valid_moves:
        white_checked = True
    if black_king_pos in white_valid_moves:
        black_checked = True

    if white_checked and black_checked:
        return "Both"
    if white_checked:
        return "White"
    if black_checked:
        return "Black"
    else:
        return "Neither"


def main():
    default = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    starting_pos = "rnbqkbnr/ppppp1pp/5p2/Q7/8/8/PPPPPPPP/RNB1KBNR w KQkq - 0 1"
    sec_pos = "rnbqkbnr/ppppp1pp/5p2/7Q/8/8/PPPPPPPP/RNB1KBNR w KQkq - 0 1"

    start = time.time()
    print('\n'.join(' '.join(str(x) for x in row) for row in fen_to_array(starting_pos)))
    print(find_valid_moves(fen_to_array(sec_pos), [3, 7]))
    print(is_valid_move(fen_to_array(starting_pos), fen_to_array(sec_pos)))
    print(rook_moves(fen_to_array(sec_pos), [0, 0]))
    print('\n'.join(' '.join(str(x) for x in row) for row in fen_to_array(sec_pos)))
    print(is_in_check(fen_to_array(sec_pos)), "is in check")
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()