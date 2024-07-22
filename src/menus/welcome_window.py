import pygame, sys
from src.colors.colors import Colors

class WelcomeWindow:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pygame.font.Font(None, 74)
        self.button_font = pygame.font.Font(None, 36)
        self.authors_font = pygame.font.Font(None, 24)
        
        self.message = "Welcome to Tetris"
        self.message_color = Colors.white
        self.authors = "@mateo1011s @diegoiza34"
        self.authors_color = Colors.gray
        
        self.start_button_text = "Start Game"
        self.exit_button_text = "Exit"
        self.scores_button_text = " Top Scores"
        
        self.start_button_color = Colors.turquoise
        self.exit_button_color = Colors.red
        self.scores_button_color = Colors.orange
        
        self.start_button_rect = pygame.Rect((self.width // 2) - 100, (self.height // 2) - 50, 200, 50)
        self.exit_button_rect = pygame.Rect((self.width // 2) - 100, (self.height // 2) + 20, 200, 50)
        self.scores_button_rect = pygame.Rect((self.width // 2)- 100, (self.height // 2) + 90, 200, 50)

    def draw(self):
        self.screen.fill(Colors.black)
        
        message_surface = self.font.render(self.message, True, self.message_color)
        message_rect = message_surface.get_rect(center=(self.width // 2, self.height // 3))
        self.screen.blit(message_surface, message_rect)

        authors_surface = self.authors_font.render(self.authors, True, self.authors_color)
        authors_rect = authors_surface.get_rect(center= (115,600))
        self.screen.blit(authors_surface, authors_rect)

        pygame.draw.rect(self.screen, self.start_button_color, self.start_button_rect)
        pygame.draw.rect(self.screen, self.exit_button_color, self.exit_button_rect)
        pygame.draw.rect(self.screen, self.scores_button_color, self.scores_button_rect)
        
        start_button_surface = self.button_font.render(self.start_button_text, True, Colors.black)
        exit_button_surface = self.button_font.render(self.exit_button_text, True, Colors.black)
        scores_button_surface = self.button_font.render(self.scores_button_text, True, Colors.black)
        
        start_button_rect = start_button_surface.get_rect(center=self.start_button_rect.center)
        exit_button_rect = exit_button_surface.get_rect(center=self.exit_button_rect.center)
        scores_button_rect = scores_button_surface.get_rect(center=self.scores_button_rect.center)
        
        
        self.screen.blit(start_button_surface, start_button_rect)
        self.screen.blit(exit_button_surface, exit_button_rect)
        self.screen.blit(scores_button_surface, scores_button_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button_rect.collidepoint(event.pos):
                return "start"
            elif self.scores_button_rect.collidepoint(event.pos):
                return "scores"
            elif self.exit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

