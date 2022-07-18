import pygame, sys
from pygame.locals import *






def main():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        CREATE_CHESSBOARD(WIDTH, HEIGHT, WINDOW)

        pygame.display.update()


if __name__ == '__main__':
    main()