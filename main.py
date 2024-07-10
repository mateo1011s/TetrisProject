import pygame,sys
from game import Game
pygame.init()

dark_blue=(44,44,127)

screen = pygame.display.set_mode((300,600))

clock=pygame.time.Clock()

game=Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    
    screen.fill(dark_blue)
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)

