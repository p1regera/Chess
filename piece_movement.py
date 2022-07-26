def is_opposite_color(piece, target_piece):
    if piece == '0' or target_piece == '0':
        return False

    return piece.islower() != target_piece.islower()


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
                    current_piece = board_array[x][y - i]
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
                elif is_opposite_color(piece, current_piece) and (piece not in ['K', 'k'] or piece in ['K', 'k']):
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
                    current_piece = board_array[x + i][y - i]
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
                elif is_opposite_color(piece, current_piece) and (piece not in ['K', 'k'] or piece in ['K', 'k']):
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

    # Coordinate offsets for the eight positions a knight can move relative to itself
    for coord_offset in [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]:
        coord_offset_x = x + coord_offset[0]
        coord_offset_y = y + coord_offset[1]
        # Using try statement to catch any index errors since the pieces cannot move off the board
        try:
            # Prevents the python wraparound for lists -> i.e. list[-1] is the last item
            if coord_offset_x < 0 or coord_offset_y < 0:
                continue
            # If the square is empty (a zero) or the opposite color piece, add it to the list of valid moves
            elif (board_array[coord_offset_x][coord_offset_y] == "0" or
                    is_opposite_color(piece, board_array[coord_offset_x][coord_offset_y])):
                valid_moves.append([coord_offset_x, coord_offset_y])
        except IndexError:
            continue

    return valid_moves


def pawn_moves(board_array, piece_pos):
    piece = board_array[piece_pos[0]][piece_pos[1]]
    valid_moves = []
    x = piece_pos[0]
    y = piece_pos[1]

    try:
        if piece == 'p':
            if board_array[x + 1][y] == '0':
                valid_moves.append([x + 1, y])
            if x == 1 and board_array[x + 2][y] == '0':
                valid_moves.append([x + 2, y])
            if is_opposite_color(piece, board_array[x + 1][y - 1]) and (y - 1) >= 0:
                valid_moves.append([x + 1, y - 1])
            if is_opposite_color(piece, board_array[x + 1][y + 1]):
                valid_moves.append([x + 1, y + 1])
        elif piece == 'P':
            if board_array[x - 1][y] == '0':
                valid_moves.append([x - 1, y])
            if x == 6 and board_array[x - 2][y] == '0':
                valid_moves.append([x - 2, y])
            if is_opposite_color(piece, board_array[x - 1][y - 1]) and (y - 1) >= 0:
                valid_moves.append([x - 1, y - 1])
            if is_opposite_color(piece, board_array[x - 1][y + 1]):
                valid_moves.append([x - 1, y + 1])
    except IndexError:
        pass

    return valid_moves


def promote(board_array):
    # Returns the location of the pawn to promote
    for i in range(0, 8):
        if board_array[0][i] == "P":
            return [0, i]
        if board_array[7][i] == "p":
            return [7, i]

    return []


def king_moves(board_array, piece_pos):
    piece = board_array[piece_pos[0]][piece_pos[1]]
    valid_moves = []
    x = piece_pos[0]
    y = piece_pos[1]

    # First take all the spaces a queen can move to
    queen_squares = queen_moves(board_array, piece_pos)
    for coord in queen_squares:
        if abs(coord[0] - x) <= 1 and abs(coord[1] - y) <= 1:
            valid_moves.append(coord)

    return valid_moves


