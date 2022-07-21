import pygame
import math
import sys
from pygame.locals import *

import board

pygame.init()

WIDTH = HEIGHT = 700
OFFSET = 0
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# set window title to "Chess"
pygame.display.set_caption("Chess")

def main():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # print("row: " + str(math.floor(pos[1] / (HEIGHT / 8))))
                # print("column: " + str(math.floor(pos[0] / (WIDTH / 8))))

                rank = math.floor(pos[1] / (HEIGHT / 8))
                file = math.floor(pos[0] / (WIDTH / 8))

                board.display_piece_movement(rank, file)

        board.CREATE_CHESSBOARD(WIDTH, HEIGHT, OFFSET, WINDOW)
        board.DISPLAY_PIECES(WIDTH, HEIGHT, OFFSET, WINDOW)

        pygame.display.update()


if __name__ == '__main__':
    main()