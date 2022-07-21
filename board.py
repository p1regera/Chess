import pygame
import sys

from pygame.locals import *

from logic import fen_to_array

WIDTH = HEIGHT = 700
OFFSET = 0
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

current_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

# load white/black pieces

blackKing = pygame.image.load("C:\\Users\\Void\\Desktop\\Game Making\\Chess\\Chess\\icons\\blackking.png")
blackKing = pygame.transform.scale(blackKing, (WIDTH / 8, HEIGHT / 8))

blackQueen = pygame.image.load("C:\\Users\\Void\\Desktop\\Game Making\\Chess\\Chess\\icons\\blackqueen.png")
blackQueen = pygame.transform.scale(blackQueen, (WIDTH / 8, HEIGHT / 8))

blackBishop = pygame.image.load("C:\\Users\\Void\\Desktop\\Game Making\\Chess\\Chess\\icons\\blackbishop.png")
blackBishop = pygame.transform.scale(blackBishop, (WIDTH / 8, HEIGHT / 8))

blackKnight = pygame.image.load("C:\\Users\\Void\\Desktop\\Game Making\\Chess\\Chess\\icons\\blackknight.png")
blackKnight = pygame.transform.scale(blackKnight, (WIDTH / 8, HEIGHT / 8))

blackRook = pygame.image.load("C:\\Users\\Void\\Desktop\\Game Making\\Chess\\Chess\\icons\\blackrook.png")
blackRook = pygame.transform.scale(blackRook, (WIDTH / 8, HEIGHT / 8))

blackPawn = pygame.image.load("C:\\Users\\Void\\Desktop\\Game Making\\Chess\\Chess\\icons\\blackpawn.png")
blackPawn = pygame.transform.scale(blackPawn, (WIDTH / 8, HEIGHT / 8))

########################################################################################################################

whiteKing = pygame.image.load("C:\\Users\\Void\\Desktop\\Game Making\\Chess\\Chess\\icons\\whiteking.png")
whiteKing = pygame.transform.scale(whiteKing, (WIDTH / 8, HEIGHT / 8))

whiteQueen = pygame.image.load("C:\\Users\\Void\\Desktop\\Game Making\\Chess\\Chess\\icons\\whitequeen.png")
whiteQueen = pygame.transform.scale(whiteQueen, (WIDTH / 8, HEIGHT / 8))

whiteBishop = pygame.image.load("C:\\Users\\Void\\Desktop\\Game Making\\Chess\\Chess\\icons\\whitebishop.png")
whiteBishop = pygame.transform.scale(whiteBishop, (WIDTH / 8, HEIGHT / 8))

whiteKnight = pygame.image.load("C:\\Users\\Void\\Desktop\\Game Making\\Chess\\Chess\\icons\\whiteknight.png")
whiteKnight = pygame.transform.scale(whiteKnight, (WIDTH / 8, HEIGHT / 8))

whiteRook = pygame.image.load("C:\\Users\\Void\\Desktop\\Game Making\\Chess\\Chess\\icons\\whiterook.png")
whiteRook = pygame.transform.scale(whiteRook, (WIDTH / 8, HEIGHT / 8))

whitePawn = pygame.image.load("C:\\Users\\Void\\Desktop\\Game Making\\Chess\\Chess\\icons\\whitepawn.png")
whitePawn = pygame.transform.scale(whitePawn, (WIDTH / 8, HEIGHT / 8))

def CREATE_CHESSBOARD(window_width, window_height, offset, surface):
    rect_width = (window_width - offset) / 8
    rect_height = (window_height - offset) / 8
    x = y = 0

    color = None
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (75, 115, 153)

    def create_horizontal_rects(x, y, color, color2):
        for i in range(8):

            rects = pygame.Rect(x, y, rect_width, rect_height)

            if i % 2 == 0:
                pygame.draw.rect(surface, color, rects)
                x += rect_width

            else:
                pygame.draw.rect(surface, color2, rects)
                x += rect_width

    x = 0

    for i in range(8):

        if i % 2 == 0:
            create_horizontal_rects(x, y, white, blue)
            y += rect_height

        if i % 2 == 1:
            create_horizontal_rects(x, y, blue, white)
            y += rect_width

def DISPLAY_PIECES(window_width, window_height, offset, surface):
    rect_width = (window_width - offset) / 8
    rect_height = (window_height - offset) / 8
    x = y = 0

    current_position_array = fen_to_array(current_position)

    # TODO: Figure out why loop needs all if, instead of elif...
    for i in range(8):
        for j in range(8):
            # black pieces
            if current_position_array[i][j] == "k":
                surface.blit(blackKing, (j * window_width / 8, i * window_height / 8))
            if current_position_array[i][j] == "q":
                surface.blit(blackQueen, (j * window_width / 8, i * window_height / 8))
            if current_position_array[i][j] == "r":
                surface.blit(blackRook, (j * window_width / 8, i * window_height / 8))
            if current_position_array[i][j] == "b":
                surface.blit(blackBishop, (j * window_width / 8, i * window_height / 8))
            if current_position_array[i][j] == "n":
                surface.blit(blackKnight, (j * window_width / 8, i * window_height / 8))
            if current_position_array[i][j] == "p":
                surface.blit(blackPawn, (j * window_width / 8, i * window_height / 8))
            # white pieces
            if current_position_array[i][j] == "K":
                surface.blit(whiteKing, (j * window_width / 8, i * window_height / 8))
            if current_position_array[i][j] == "Q":
                surface.blit(whiteQueen, (j * window_width / 8, i * window_height / 8))
            if current_position_array[i][j] == "R":
                surface.blit(whiteRook, (j * window_width / 8, i * window_height / 8))
            if current_position_array[i][j] == "B":
                surface.blit(whiteBishop, (j * window_width / 8, i * window_height / 8))
            if current_position_array[i][j] == "N":
                surface.blit(whiteKnight, (j * window_width / 8, i * window_height / 8))
            if current_position_array[i][j] == "P":
                surface.blit(whitePawn, (j * window_width / 8, i * window_height / 8))

def display_piece_movement(rank, file):
    current_position_array = fen_to_array(current_position)

    print(current_position_array[rank][file])