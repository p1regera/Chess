import pygame
import sys
from pygame.locals import *

import board

pygame.init()

WIDTH = HEIGHT = 700
OFFSET = 20
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        board.CREATE_CHESSBOARD(WIDTH, HEIGHT, OFFSET, WINDOW)

        pygame.display.update()


if __name__ == '__main__':
    main()