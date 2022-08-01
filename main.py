import pygame
import sys

import board

pygame.init()

# set window title to "Chess"
pygame.display.set_caption("Chess")
pygame.display.set_icon(board.blackPawn)

FPS = 300
fpsClock = pygame.time.Clock()

def main():
    while True:
        board.CREATE_CHESSBOARD()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not board.isCheckmate and not board.isStalemate:
                mousePos = pygame.mouse.get_pos()
                board.MOVE_PIECES(mousePos)
            if event.type == pygame.KEYDOWN:
                # press R to reset board to starting position
                if event.key == pygame.K_r:
                    board.RESET_PIECES()
                # press left arrow to go back one move
                if event.key == pygame.K_LEFT:
                    board.MAKE_PREVIOUS_TURN()

        board.DISPLAY_PIECE_EFFECTS()
        board.DISPLAY_PIECES()
        board.DISPLAY_BOARD_EFFECTS()

        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()