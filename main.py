import pygame
import sys

import board

pygame.init()

# set window title to "Chess"
pygame.display.set_caption("Chess")
pygame.display.set_icon(board.blackPawn)

def main():
    while True:
        board.CREATE_CHESSBOARD()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                board.MOVE_PIECES(mousePos)
            if event.type == pygame.KEYDOWN:
                # press R to reset board to starting position
                if event.key == pygame.K_r:
                    board.RESET_PIECES()

        board.DISPLAY_EFFECTS()
        board.DISPLAY_PIECES()

        pygame.display.update()

if __name__ == '__main__':
    main()