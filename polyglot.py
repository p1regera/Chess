import chess
import chess.polyglot

def get_best_move(fen_string):
    board = chess.Board(fen_string)
    
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

    return new_fen
