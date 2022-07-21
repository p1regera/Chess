import pygame
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

        board.CREATE_CHESSBOARD(WIDTH, HEIGHT, OFFSET, WINDOW)

        pygame.display.update()


if __name__ == '__main__':
    main()