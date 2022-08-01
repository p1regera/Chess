import pygame

# window / pygame variables
WIDTH = HEIGHT = 800
OFFSET = 0
RECT_WIDTH = (WIDTH - OFFSET) / 8
RECT_HEIGHT = (HEIGHT - OFFSET) / 8
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TRANSPARENT = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

# game status
bMate = pygame.image.load("./effects/bMate.png")
bMate = pygame.transform.scale(bMate, (WIDTH / 24, HEIGHT / 24))

wMate = pygame.image.load("./effects/wMate.png")
wMate = pygame.transform.scale(wMate, (WIDTH / 24, HEIGHT / 24))

stalemate = pygame.image.load("./effects/stalemate.png")
stalemate = pygame.transform.scale(stalemate, (WIDTH / 24, HEIGHT / 24))

won = pygame.image.load("./effects/won.png")
won = pygame.transform.scale(won, (WIDTH / 24, HEIGHT / 24))

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

# load all pieces
preferredPieces = None

# base theme
baseTheme = "base"

# black pieces
baseBlackKing = pygame.image.load("pieces/" + baseTheme + "/bk.png")
baseBlackKing = pygame.transform.scale(baseBlackKing, (WIDTH / 8, HEIGHT / 8))

baseBlackQueen = pygame.image.load("pieces/" + baseTheme + "/bq.png")
baseBlackQueen = pygame.transform.scale(baseBlackQueen, (WIDTH / 8, HEIGHT / 8))

baseBlackBishop = pygame.image.load("pieces/" + baseTheme + "/bb.png")
baseBlackBishop = pygame.transform.scale(baseBlackBishop, (WIDTH / 8, HEIGHT / 8))

baseBlackKnight = pygame.image.load("pieces/" + baseTheme + "/bn.png")
baseBlackKnight = pygame.transform.scale(baseBlackKnight, (WIDTH / 8, HEIGHT / 8))

baseBlackRook = pygame.image.load("pieces/" + baseTheme + "/br.png")
baseBlackRook = pygame.transform.scale(baseBlackRook, (WIDTH / 8, HEIGHT / 8))

baseBlackPawn = pygame.image.load("pieces/" + baseTheme + "/bp.png")
baseBlackPawn = pygame.transform.scale(baseBlackPawn, (WIDTH / 8, HEIGHT / 8))

# white pieces

baseWhiteKing = pygame.image.load("pieces/" + baseTheme + "/wk.png")
baseWhiteKing = pygame.transform.scale(baseWhiteKing, (WIDTH / 8, HEIGHT / 8))

baseWhiteQueen = pygame.image.load("pieces/" + baseTheme + "/wq.png")
baseWhiteQueen = pygame.transform.scale(baseWhiteQueen, (WIDTH / 8, HEIGHT / 8))

baseWhiteBishop = pygame.image.load("pieces/" + baseTheme + "/wb.png")
baseWhiteBishop = pygame.transform.scale(baseWhiteBishop, (WIDTH / 8, HEIGHT / 8))

baseWhiteKnight = pygame.image.load("pieces/" + baseTheme + "/wn.png")
baseWhiteKnight = pygame.transform.scale(baseWhiteKnight, (WIDTH / 8, HEIGHT / 8))

baseWhiteRook = pygame.image.load("pieces/" + baseTheme + "/wr.png")
baseWhiteRook = pygame.transform.scale(baseWhiteRook, (WIDTH / 8, HEIGHT / 8))

baseWhitePawn = pygame.image.load("pieces/" + baseTheme + "/wp.png")
baseWhitePawn = pygame.transform.scale(baseWhitePawn, (WIDTH / 8, HEIGHT / 8))

# wood theme
woodTheme = "wood"

# black pieces
woodBlackKing = pygame.image.load("pieces/" + woodTheme + "/bk.png")
woodBlackKing = pygame.transform.scale(woodBlackKing, (WIDTH / 8, HEIGHT / 8))

woodBlackQueen = pygame.image.load("pieces/" + woodTheme + "/bq.png")
woodBlackQueen = pygame.transform.scale(woodBlackQueen, (WIDTH / 8, HEIGHT / 8))

woodBlackBishop = pygame.image.load("pieces/" + woodTheme + "/bb.png")
woodBlackBishop = pygame.transform.scale(woodBlackBishop, (WIDTH / 8, HEIGHT / 8))

woodBlackKnight = pygame.image.load("pieces/" + woodTheme + "/bn.png")
woodBlackKnight = pygame.transform.scale(woodBlackKnight, (WIDTH / 8, HEIGHT / 8))

woodBlackRook = pygame.image.load("pieces/" + woodTheme + "/br.png")
woodBlackRook = pygame.transform.scale(woodBlackRook, (WIDTH / 8, HEIGHT / 8))

woodBlackPawn = pygame.image.load("pieces/" + woodTheme + "/bp.png")
woodBlackPawn = pygame.transform.scale(woodBlackPawn, (WIDTH / 8, HEIGHT / 8))

# white pieces

woodWhiteKing = pygame.image.load("pieces/" + woodTheme + "/wk.png")
woodWhiteKing = pygame.transform.scale(woodWhiteKing, (WIDTH / 8, HEIGHT / 8))

woodWhiteQueen = pygame.image.load("pieces/" + woodTheme + "/wq.png")
woodWhiteQueen = pygame.transform.scale(woodWhiteQueen, (WIDTH / 8, HEIGHT / 8))

woodWhiteBishop = pygame.image.load("pieces/" + woodTheme + "/wb.png")
woodWhiteBishop = pygame.transform.scale(woodWhiteBishop, (WIDTH / 8, HEIGHT / 8))

woodWhiteKnight = pygame.image.load("pieces/" + woodTheme + "/wn.png")
woodWhiteKnight = pygame.transform.scale(woodWhiteKnight, (WIDTH / 8, HEIGHT / 8))

woodWhiteRook = pygame.image.load("pieces/" + woodTheme + "/wr.png")
woodWhiteRook = pygame.transform.scale(woodWhiteRook, (WIDTH / 8, HEIGHT / 8))

woodWhitePawn = pygame.image.load("pieces/" + woodTheme + "/wp.png")
woodWhitePawn = pygame.transform.scale(woodWhitePawn, (WIDTH / 8, HEIGHT / 8))


# TODO: figure out how to streamline changing piece theme (i.e. changing 1 variable instead of 12...)
preferredWhitePawn = woodWhitePawn
preferredWhiteRook = woodWhiteRook
preferredWhiteBishop = woodWhiteBishop
preferredWhiteKnight = woodWhiteKnight
preferredWhiteQueen = woodWhiteQueen
preferredWhiteKing = woodWhiteKing

preferredBlackPawn = woodBlackPawn
preferredBlackRook = woodBlackRook
preferredBlackBishop = woodBlackBishop
preferredBlackKnight = woodBlackKnight
preferredBlackQueen = woodBlackQueen
preferredBlackKing = woodBlackKing

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