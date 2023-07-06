import pygame
import sys

import board
import engine

pygame.init()

# set window title to "Chess"
pygame.display.set_caption("Chess")
pygame.display.set_icon(board.blackPawn)

FPS = 300
fpsClock = pygame.time.Clock()

def main():
    ismainScreenRunning = True
    isGamePageRunning = False
    game_mode = "engine"


    # create main screen, with two buttons, one for 2 players, one for engine
    mainScreen = pygame.display.set_mode((board.WIDTH, board.HEIGHT))
    mainScreen.blit(board.preferredBoard, (0, 0))

    while ismainScreenRunning:
        # create 2 players button
        twoPlayersButton = pygame.Rect(board.WIDTH / 2 - board.WIDTH / 8, board.HEIGHT / 2 - board.HEIGHT / 8, board.WIDTH / 4, board.HEIGHT / 8)
        pygame.draw.rect(mainScreen, (255, 255, 255), twoPlayersButton)

        # create engine button
        engineButton = pygame.Rect(board.WIDTH / 2 - board.WIDTH / 8, board.HEIGHT / 2 + board.HEIGHT / 8, board.WIDTH / 4, board.HEIGHT / 8)
        pygame.draw.rect(mainScreen, (255, 255, 255), engineButton)

        # create text for buttons
        twoPlayersText = pygame.font.SysFont("Arial", 30).render("2 Players", True, (0, 0, 0))
        engineText = pygame.font.SysFont("Arial", 30).render("Engine", True, (0, 0, 0))

        # display text on buttons
        mainScreen.blit(twoPlayersText, (board.WIDTH / 2 - board.WIDTH / 8 + board.WIDTH / 32, board.HEIGHT / 2 - board.HEIGHT / 8 + board.HEIGHT / 32))
        mainScreen.blit(engineText, (board.WIDTH / 2 - board.WIDTH / 8 + board.WIDTH / 32, board.HEIGHT / 2 + board.HEIGHT / 8 + board.HEIGHT / 32))
        
        # get mouse position
        mousePos = pygame.mouse.get_pos()

        # check if button is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if 2 players button is clicked, start 2 players game
            if event.type == pygame.MOUSEBUTTONDOWN and twoPlayersButton.collidepoint(mousePos):
                ismainScreenRunning = False
                isGamePageRunning = True
                game_mode = "player"
            # if engine button is clicked, start engine game
            if event.type == pygame.MOUSEBUTTONDOWN and engineButton.collidepoint(mousePos):
                ismainScreenRunning = False
                isGamePageRunning = True
                game_mode = "engine"
        
        pygame.display.update()
        fpsClock.tick(FPS)


    while isGamePageRunning:
        board.CREATE_CHESSBOARD()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 2 players
            if event.type == pygame.MOUSEBUTTONDOWN and not board.isCheckmate and not board.isStalemate:
                engine.find_valid_board_states()
                mousePos = pygame.mouse.get_pos()
                board.MOVE_PIECES(mousePos)
            # if the game mode is engine, let the engine move and change the board position
            if game_mode == "engine" and board.colorTurn == "b" and not board.isCheckmate and not board.isStalemate:
                board.DISPLAY_PIECE_EFFECTS()
                board.DISPLAY_PIECES()
                board.DISPLAY_BOARD_EFFECTS()
                pygame.display.update()
                fpsClock.tick(FPS)

                board.ENGINE_MOVE_PIECE()
                board.PLAY_MOVE_SOUND()

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