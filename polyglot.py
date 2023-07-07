import chess
import chess.polyglot

def get_best_move(fen_string, opening_book):
    castling_options = [' b KQkq - 0 1', ' b KQk - 0 1', ' b KQq - 0 1', ' b KQ - 0 1']
    best_move = None
    best_weight = 0
    best_new_fen = None
    engine_file = "openingbooks/" + opening_book + ".bin"
    with chess.polyglot.open_reader(engine_file) as reader:
        for castle_option in castling_options:
            fen = fen_string + castle_option
            board = chess.Board(fen)
            try:
                entries = list(reader.find_all(board))
                print(f"For castling option '{castle_option}', number of entries found in book: {len(entries)}")
                main_entry = reader.weighted_choice(board)
                move = main_entry.move
                if main_entry.weight > best_weight:
                    best_move = move
                    best_weight = main_entry.weight
                    board.push(move)  # Apply the move to the board
                    best_new_fen = board.fen()  # Get the FEN string of the new board
            except IndexError:
                print(f"No opening move found in book for castling option '{castle_option}'.")
                
    return best_new_fen

# def get_best_move(fen_string):
#     castle1 = fen_string + ' b KQkq - 0 1'
#     castle2 = fen_string + ' b KQk - 0 1'
#     castle3 = fen_string + ' b KQq - 0 1'
#     castle4 = fen_string + ' b KQ - 0 1'
#     board = chess.Board(castle1)
#     board2 = chess.Board(castle2)
#     board3 = chess.Board(castle3)
#     board4 = chess.Board(castle4)
    
#     with chess.polyglot.open_reader("openingbooks/lichess_huge.bin") as reader:
#         try:
#             entries = list(reader.find_all(board))
#             print(f"Number of entries found in book: {len(entries)}")
#             main_entry = reader.weighted_choice(board)
#             move = main_entry.move
#             board.push(move)  # Apply the move to the board
#             new_fen = board.fen()  # Get the FEN string of the new board
#         except IndexError:
#             print("No opening move found in book.")
#             new_fen = None
