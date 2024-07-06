import pygame,sys
from grid import Grid

pygame.init()

darkBlue=(44,44,127)

screen= pygame.display.set_mode((300,600))

clock=pygame.time.Clock()

game_grid=Grid()
game_grid.print_grid()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit() 
    
    screen.fill(darkBlue)
    game_grid.draw(screen)
    pygame.display.update()
    clock.tick(60)

