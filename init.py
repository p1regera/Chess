import pygame

# window / pygame variables
WIDTH = HEIGHT = 800
OFFSET = 0
RECT_WIDTH = (WIDTH - OFFSET) / 8
RECT_HEIGHT = (HEIGHT - OFFSET) / 8
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TRANSPARENT = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

# load in image of chess board, stores your preferred board
preferredBoard = None

blueBoard = pygame.image.load("./themes/blueBoard.png")
blueBoard = pygame.transform.scale(blueBoard, (WIDTH, HEIGHT))

# default board
newspaperBoard = pygame.image.load("./themes/newspaperBoard.png")
newspaperBoard = pygame.transform.scale(newspaperBoard, (WIDTH, HEIGHT))

tournamentBoard = pygame.image.load("./themes/tournamentBoard.png")
tournamentBoard = pygame.transform.scale(tournamentBoard, (WIDTH, HEIGHT))

woodBoard = pygame.image.load("./themes/woodBoard.png")
woodBoard = pygame.transform.scale(woodBoard, (WIDTH, HEIGHT))

preferredBoard = woodBoard

# game status
bMate = pygame.image.load("./effects/bMate.png")
bMate = pygame.transform.scale(bMate, (WIDTH / 24, HEIGHT / 24))

wMate = pygame.image.load("./effects/wMate.png")
wMate = pygame.transform.scale(wMate, (WIDTH / 24, HEIGHT / 24))

stalemate = pygame.image.load("./effects/stalemate.png")
stalemate = pygame.transform.scale(stalemate, (WIDTH / 24, HEIGHT / 24))

won = pygame.image.load("./effects/won.png")
won = pygame.transform.scale(won, (WIDTH / 24, HEIGHT / 24))

# load white/black pieces
blackKing = pygame.image.load("pieces/bk.png")
blackKing = pygame.transform.scale(blackKing, (WIDTH / 8, HEIGHT / 8))

blackQueen = pygame.image.load("pieces/bq.png")
blackQueen = pygame.transform.scale(blackQueen, (WIDTH / 8, HEIGHT / 8))

blackBishop = pygame.image.load("pieces/bb.png")
blackBishop = pygame.transform.scale(blackBishop, (WIDTH / 8, HEIGHT / 8))

blackKnight = pygame.image.load("pieces/bn.png")
blackKnight = pygame.transform.scale(blackKnight, (WIDTH / 8, HEIGHT / 8))

blackRook = pygame.image.load("pieces/br.png")
blackRook = pygame.transform.scale(blackRook, (WIDTH / 8, HEIGHT / 8))

blackPawn = pygame.image.load("pieces/bp.png")
blackPawn = pygame.transform.scale(blackPawn, (WIDTH / 8, HEIGHT / 8))

########################################################################################################################

whiteKing = pygame.image.load("pieces/wk.png")
whiteKing = pygame.transform.scale(whiteKing, (WIDTH / 8, HEIGHT / 8))

whiteQueen = pygame.image.load("pieces/wq.png")
whiteQueen = pygame.transform.scale(whiteQueen, (WIDTH / 8, HEIGHT / 8))

whiteBishop = pygame.image.load("pieces/wb.png")
whiteBishop = pygame.transform.scale(whiteBishop, (WIDTH / 8, HEIGHT / 8))

whiteKnight = pygame.image.load("pieces/wn.png")
whiteKnight = pygame.transform.scale(whiteKnight, (WIDTH / 8, HEIGHT / 8))

whiteRook = pygame.image.load("pieces/wr.png")
whiteRook = pygame.transform.scale(whiteRook, (WIDTH / 8, HEIGHT / 8))

whitePawn = pygame.image.load("pieces/wp.png")
whitePawn = pygame.transform.scale(whitePawn, (WIDTH / 8, HEIGHT / 8))

############################################################################

pygame.mixer.init()

# load game sounds
pygame.mixer.music.load("./sfx/gamestart.wav")
gameStartSound = pygame.mixer.Sound("./sfx/gamestart.wav")
pygame.mixer.Sound.play(gameStartSound)

pygame.mixer.music.load("./sfx/regmove.wav")
moveSound = pygame.mixer.Sound("./sfx/regmove.wav")

pygame.mixer.music.load("./sfx/capture.wav")
captureSound = pygame.mixer.Sound("./sfx/capture.wav")

pygame.mixer.music.load("./sfx/castling.wav")
castlingSound = pygame.mixer.Sound("./sfx/castling.wav")

pygame.mixer.music.load("./sfx/check.wav")
checkSound = pygame.mixer.Sound("./sfx/check.wav")

pygame.mixer.music.load("./sfx/checkmate.wav")
checkmateSound = pygame.mixer.Sound("./sfx/checkmate.wav")

pygame.mixer.music.load("./sfx/stalemate.wav")
stalemateSound = pygame.mixer.Sound("./sfx/stalemate.wav")