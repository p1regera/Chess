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

def is_valid_move(previous_fen, current_fen):
    # Turn FEN into array
    prev_board = fen_to_array(previous_fen)
    current_board = fen_to_array(current_fen)

    # Find which piece moves, and the starting and end position

    pass

def find_valid_moves(board_array, piece_pos):
    # returns 2d list of all valid moves a piece can make i.e. [[x,y], [x,y], ..]
    piece = board_array[piece_pos[0]][piece_pos[1]]

    if piece in ['P', 'p']:
        return None
    elif piece in ['R', 'r']:
        return rook_moves(board_array, piece_pos)
    elif piece in ['N', 'n']:
        return None
    elif piece in ['B', 'b']:
        return bishop_moves(board_array, piece_pos)
    elif piece in ['Q', 'q']:
        return queen_moves(board_array, piece_pos)
    elif piece in ['K', 'k']:
        return None
    else:
        return None

    # match piece:
    #     case 'P':
    #         pass
    #     case 'R':
    #         pass
    #     case 'N':
    #         pass
    #     case 'B':
    #         pass
    #     case 'Q':
    #         pass
    #     case 'K':
    #         pass

def main():

    starting_pos = "rnbqkbnr/pppppppp/8/8/4q3/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    start = time.time()
    print('\n'.join(' '.join(str(x) for x in row) for row in fen_to_array(starting_pos)))
    print(find_valid_moves(fen_to_array(starting_pos), [4, 4]))
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    main()