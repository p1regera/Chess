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
    opening_book = "lichess"

    # create main screen, with two buttons, one for 2 players, one for engine
    mainScreen = pygame.display.set_mode((board.WIDTH, board.HEIGHT))
    mainScreen.blit(board.bg_image, (0, 0))

    # button dimensions
    button_width = board.WIDTH / 4
    button_height = board.HEIGHT / 8

    # Initialize button states
    button_states = {1: False, 2: False, 3: False}

    # Create buttons
    button1 = pygame.Rect(board.WIDTH / 6 - button_width / 2, board.HEIGHT - board.HEIGHT / 8, button_width, button_height)
    button2 = pygame.Rect(board.WIDTH / 2 - button_width / 2, board.HEIGHT - board.HEIGHT / 8, button_width, button_height)
    button3 = pygame.Rect(5 * board.WIDTH / 6 - button_width / 2, board.HEIGHT - board.HEIGHT / 8, button_width, button_height)

    while ismainScreenRunning:
        # create buttons
        twoPlayersButton = pygame.Rect(board.WIDTH / 2 - board.WIDTH / 8, board.HEIGHT / 2 - board.HEIGHT / 8, board.WIDTH / 4, board.HEIGHT / 8)
        engineButton = pygame.Rect(board.WIDTH / 2 - board.WIDTH / 8, board.HEIGHT / 2 + board.HEIGHT / 8, board.WIDTH / 4, board.HEIGHT / 8)

        pygame.draw.rect(mainScreen, (255, 0, 0) if button_states[1] else (255, 255, 255), button1)
        pygame.draw.rect(mainScreen, (255, 0, 0) if button_states[2] else (255, 255, 255), button2)
        pygame.draw.rect(mainScreen, (255, 0, 0) if button_states[3] else (255, 255, 255), button3)

        # Display button labels
        button1Text = pygame.font.SysFont("Arial", 20).render("Lichess", True, (0, 0, 0))
        button2Text = pygame.font.SysFont("Arial", 20).render("Baron30", True, (0, 0, 0))
        button3Text = pygame.font.SysFont("Arial", 20).render("Codekiddy", True, (0, 0, 0))
        mainScreen.blit(button1Text, (button1.x + button1.width / 2, button1.y + button1.height / 2))
        mainScreen.blit(button2Text, (button2.x + button2.width / 2, button2.y + button2.height / 2))
        mainScreen.blit(button3Text, (button3.x + button3.width / 2, button3.y + button3.height / 2))


        # get mouse position
        mousePos = pygame.mouse.get_pos()
        
        # change image if mouse is over the button
        mainScreen.blit(board.twoplayer_img, twoPlayersButton)
            
        mainScreen.blit(board.engine_img, engineButton)

        # create text for buttons
        twoPlayersText = pygame.font.SysFont("Arial", 30).render("2 Players", True, (0, 0, 0))
        engineText = pygame.font.SysFont("Arial", 30).render("Engine", True, (0, 0, 0))

        # display text on buttons
        mainScreen.blit(twoPlayersText, (board.WIDTH / 2 - board.WIDTH / 8 + board.WIDTH / 32 * 3.5, board.HEIGHT / 2 - board.HEIGHT / 8 + board.HEIGHT / 32))
        mainScreen.blit(engineText, (board.WIDTH / 2 - board.WIDTH / 8 + board.WIDTH / 32 * 3.5, board.HEIGHT / 2 + board.HEIGHT / 8 + board.HEIGHT / 32))
        
        # get mouse position
        mousePos = pygame.mouse.get_pos()

        # check if button is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

           
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mousePos):
                    opening_book = "lichess"
                    button_states[1] = not button_states[1]
                    button_states[2] = False
                    button_states[3] = False
                elif button2.collidepoint(mousePos):
                    opening_book = "baron30"
                    button_states[2] = not button_states[2]
                    button_states[1] = False
                    button_states[3] = False
                elif button3.collidepoint(mousePos):
                    opening_book = "codekiddy"
                    button_states[3] = not button_states[3]
                    button_states[1] = False
                    button_states[2] = False
        
                # if 2 players button is clicked, start 2 players game
                if twoPlayersButton.collidepoint(mousePos):
                    ismainScreenRunning = False
                    isGamePageRunning = True
                    game_mode = "player"
                # if engine button is clicked, start engine game
                if engineButton.collidepoint(mousePos):
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
                board.ENGINE_MOVE_PIECE(opening_book)


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