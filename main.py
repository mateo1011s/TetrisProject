import pygame,sys
from src.game.game import Game
from src.colors.colors import Colors
from src.menus.welcome_window import WelcomeWindow
from src.menus.game_over_window import GameOverWindow

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next Block", True, Colors.white)

score_rect = pygame.Rect(320, 160 , 170, 60)
next_rect = pygame.Rect(320, 340 , 170, 180)

screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("Tetris Game")

clock=pygame.time.Clock()



GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 600)

def reset_game():
    global game, welcome_window, game_over_window, show_welcome, show_game_over
    game = Game()
    welcome_window = WelcomeWindow(screen)
    game_over_window = GameOverWindow(screen)
    show_welcome = True
    show_game_over = False

reset_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if show_welcome:
            if event.type == pygame.MOUSEBUTTONDOWN:
                action = welcome_window.handle_event(event)
                if action == "start":
                    show_welcome = False
        elif show_game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                action = game_over_window.handle_event(event)
                if action == "main_menu":
                    reset_game()
                elif action == "restart":
                    show_game_over = False
                    game.game_over = False
                    game.reset()
        else: 
            if event.type == pygame.KEYDOWN:
                if game.game_over:
                    show_game_over = True
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
    
    if show_welcome:
        welcome_window.draw()
    elif show_game_over:
        game_over_window.draw()
    else:
        score_value_surface = title_font.render(str(game.score), True, Colors.white)
        screen.fill(Colors.dark_blue)
        screen.blit(score_surface, (365, 100, 50, 50))
        screen.blit(next_surface, (335, 280, 50, 50))
        pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,
        centery = score_rect.centery))
        pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
        game.draw(screen)
    
    pygame.display.update()
    clock.tick(60)

