import chess
import chess.polyglot

def get_best_move(fen_string, opening_book):
    board = chess.Board(fen_string)
    
    if opening_book == "lichess":
        with chess.polyglot.open_reader("openingbooks/lichess_huge.bin") as reader:
            try:
                entries = list(reader.find_all(board))
                print(f"Number of entries found in book: {len(entries)}")
                main_entry = reader.weighted_choice(board)
                move = main_entry.move
                board.push(move)  # Apply the move to the board
                new_fen = board.fen()  # Get the FEN string of the new board
            except IndexError:
                print("No opening move found in book.")
                new_fen = None
    elif opening_book == "baron30":
        with chess.polyglot.open_reader("openingbooks/baron30.bin") as reader:
            try:
                entries = list(reader.find_all(board))
                print(f"Number of entries found in book: {len(entries)}")
                main_entry = reader.weighted_choice(board)
                move = main_entry.move
                board.push(move)  # Apply the move to the board
                new_fen = board.fen()  # Get the FEN string of the new board
            except IndexError:
                print("No opening move found in book.")
                new_fen = None
    elif opening_book == "codekiddy":
        with chess.polyglot.open_reader("openingbooks/codekiddy.bin") as reader:
            try:
                entries = list(reader.find_all(board))
                print(f"Number of entries found in book: {len(entries)}")
                main_entry = reader.weighted_choice(board)
                move = main_entry.move
                board.push(move)  # Apply the move to the board
                new_fen = board.fen()  # Get the FEN string of the new board
            except IndexError:
                print("No opening move found in book.")
                new_fen = None
    else:
        print(f"Opening book {opening_book} not found.")

    return new_fen
