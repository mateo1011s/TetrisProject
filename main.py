import pygame,sys
from src.game.game import Game

pygame.init()
dark_blue=(44,44,127)

screen = pygame.display.set_mode((300,600))
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
                
    screen.fill(dark_blue)
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)

