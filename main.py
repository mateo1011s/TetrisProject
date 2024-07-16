import pygame,sys
from src.game.game import Game
from src.colors.colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next Block", True, Colors.white)

score_rect = pygame.Rect(320, 160 , 170, 60)
next_rect = pygame.Rect(320, 340 , 170, 180)

screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("Tetris Game")

clock=pygame.time.Clock()

game=Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 600)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s and game.game_over == False:
                game.move_down()
            if event.key == pygame.K_UP or event.key == pygame.K_w and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
                
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 100, 50, 50))
    screen.blit(next_surface, (335, 280, 50, 50))
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)

