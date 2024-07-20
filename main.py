import pygame,sys
from src.game.events import EventsInGame

pygame.init()

screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("Tetris Game")

clock=pygame.time.Clock()

events = EventsInGame(screen)

while True:
    events.process_events(screen)
    
    pygame.display.update()
    clock.tick(60)

