import pygame,sys

pygame.init()

darkBlue=(44,44,127)

screen= pygame.display.set_mode((300,600))

clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit() 
    
    screen.fill(darkBlue)
    pygame.display.update()
    clock.tick(60)
