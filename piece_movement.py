import re
import time


def is_opposite_color(piece, target_piece):
    if piece.islower() != target_piece.islower():
        return True
    else:
        return False

def rook_moves(board_array, piece_pos):
    piece = board_array[piece_pos[0]][piece_pos[1]]
    valid_moves = []
    x = piece_pos[0]
    y = piece_pos[1]
    for direction in ["right", "down", "left", "up"]:
        for i in range(1, 8):
            try:
                if direction == "right":
                    current_piece = board_array[x][y + i]
                    target_x = x
                    target_y = y + i
                elif direction == "down":
                    current_piece = board_array[x + i][y]
                    target_x = x + i
                    target_y = y
                elif direction == "left":
                    current_piece = board_array[x][y - 1]
                    target_x = x
                    target_y = y - i
                    if target_y < 0:
                        break
                else:
                    current_piece = board_array[x - i][y]
                    target_x = x - i
                    target_y = y
                    if target_x < 0:
                        break

                if current_piece == '0':
                    valid_moves.append([target_x, target_y])
                elif is_opposite_color(piece, current_piece):
                    valid_moves.append([target_x, target_y])
                    break
                else:
                    break
            except IndexError:
                break

    return valid_moves

def bishop_moves(board_array, piece_pos):
    piece = board_array[piece_pos[0]][piece_pos[1]]
    valid_moves = []
    x = piece_pos[0]
    y = piece_pos[1]
    for direction in ["up-right", "down-right", "down-left", "up-left"]:
        for i in range(1, 8):
            try:
                if direction == "up-right":
                    current_piece = board_array[x - i][y + i]
                    target_x = x - i
                    target_y = y + i
                    if target_x < 0:
                        break
                elif direction == "down-right":
                    current_piece = board_array[x + i][y + i]
                    target_x = x + i
                    target_y = y + i
                elif direction == "down-left":
                    current_piece = board_array[x + i][y - 1]
                    target_x = x + i
                    target_y = y - i
                    if target_y < 0:
                        break
                else:
                    current_piece = board_array[x - i][y - i]
                    target_x = x - i
                    target_y = y - i
                    if target_x < 0 or target_y < 0:
                        break

                if current_piece == '0':
                    valid_moves.append([target_x, target_y])
                elif is_opposite_color(piece, current_piece):
                    valid_moves.append([target_x, target_y])
                    break
                else:
                    break
            except IndexError:
                break

    return valid_moves

def queen_moves(board_array, piece_pos):
    # Combining the rook and bishop moves since a queen moves like both pieces
    valid_moves = rook_moves(board_array, piece_pos)
    bishop_temp = bishop_moves(board_array, piece_pos)
    for move in bishop_temp:
        valid_moves.append(move)

    return valid_moves

def knight_moves(board_array, piece_pos):
    piece = board_array[piece_pos[0]][piece_pos[1]]
    valid_moves = []
    x = piece_pos[0]
    y = piece_pos[1]
    pass