import pygame,sys
from src.game.events import EventsInGame

pygame.init()

screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("Tetris Game")

clock=pygame.time.Clock()

events = EventsInGame(screen)

while True:
    try:
        events.process_events(screen)
        pygame.display.update()
        clock.tick(60)
    except pygame.error as e:
        print(f"Pygame error: {e}")
        break
    except Exception as e:
        print(f"Unexpected error: {e}")
        break

pygame.quit()