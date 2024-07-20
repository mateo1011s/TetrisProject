import pygame
from src.colors.colors import Colors
from src.game.game import Game

class InterfaceUser:
    def __init__(self, screen):
        self.title_font = pygame.font.Font(None, 40)
        self.score_surface = self.title_font.render("Score", True, Colors.white)
        self.next_surface = self.title_font.render("Next Block", True, Colors.white)

        self.score_rect = pygame.Rect(320, 160 , 170, 60)
        self.next_rect = pygame.Rect(320, 340 , 170, 180)

        self.game = Game(screen)
    
    def draw(self, screen):
        score_value_surface = self.title_font.render(str(self.game.score), True, Colors.white)
        screen.fill(Colors.dark_blue)
        screen.blit(self.score_surface, (365, 100, 50, 50))
        screen.blit(self.next_surface, (335, 280, 50, 50))
        pygame.draw.rect(screen, Colors.light_blue, self.score_rect, 0, 10)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx = self.score_rect.centerx,
        centery = self.score_rect.centery))
        pygame.draw.rect(screen, Colors.light_blue, self.next_rect, 0, 10)

    def reset_game(self):
        self.game.reset()