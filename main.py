import pygame,sys
from src.game.interface_user import InterfaceUser

pygame.init()

screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("Tetris Game")

clock=pygame.time.Clock()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 600)

interface = InterfaceUser(screen)
game = interface.game

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game.show_welcome:
            if event.type == pygame.MOUSEBUTTONDOWN:
                action = game.welcome_window.handle_event(event)
                if action == "start":
                    game.show_welcome = False
        elif game.show_game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                action = game.game_over_window.handle_event(event)
                if action == "main_menu":
                    game.show_welcome = True
                    game.show_game_over = False
                    interface.reset_game()
                elif action == "restart":
                    game.show_game_over = False
                    game.reset()
        else: 
            if event.type == pygame.KEYDOWN:
                if game.game_over:
                    game.show_game_over = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a and game.game_over == False:
                    game.move_left()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d and game.game_over == False:
                    game.move_right()
                if event.key == pygame.K_DOWN or event.key == pygame.K_s and game.game_over == False:
                    game.move_down()
                    game.update_score(0, 1)
                if event.key == pygame.K_UP or event.key == pygame.K_w and game.game_over == False:
                    game.rotate()
            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()
    
    if game.show_welcome:
        game.welcome_window.draw()
    elif game.show_game_over:
        game.game_over_window.draw()
    else:
        interface.draw(screen)
        game.draw(screen)
    
    pygame.display.update()
    clock.tick(60)

