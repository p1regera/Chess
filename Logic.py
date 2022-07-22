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


def is_valid_move(prev_board_array, cur_board_array):
    # Find which piece moves, and the starting and end position
    prev_piece_pos = []
    cur_piece_pos = []
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
    if cur_pos in find_valid_moves(prev_board_array, prev_pos):
        return True
    else:
        return False


def find_valid_moves(board_array, piece_pos):
    # returns 2d list of all valid moves a piece can make i.e. [[x,y], [x,y], ..]
    piece = board_array[piece_pos[0]][piece_pos[1]]

    if piece in ['P', 'p']:
        return rook_moves(board_array, piece_pos)
    elif piece in ['R', 'r']:
        return rook_moves(board_array, piece_pos)
    elif piece in ['N', 'n']:
        return knight_moves(board_array, piece_pos)
    elif piece in ['B', 'b']:
        return bishop_moves(board_array, piece_pos)
    elif piece in ['Q', 'q']:
        return queen_moves(board_array, piece_pos)
    elif piece in ['K', 'k']:
        return queen_moves(board_array, piece_pos)
    else:
        return None


def main():

    starting_pos = "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 1"
    sec_pos = "rnbqkbnr/pppppppp/8/3Q4/3P4/8/PPP1PPPP/RNB1KBNR w KQkq - 0 1"

    start = time.time()
    print('\n'.join(' '.join(str(x) for x in row) for row in fen_to_array(starting_pos)))
    print(find_valid_moves(fen_to_array(starting_pos), [7, 3]))
    print(is_valid_move(fen_to_array(starting_pos), fen_to_array(sec_pos)))
    print('\n'.join(' '.join(str(x) for x in row) for row in fen_to_array(sec_pos)))
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()