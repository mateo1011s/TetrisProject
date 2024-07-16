import pygame, sys
from src.colors.colors import Colors

class WelcomeWindow:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pygame.font.Font(None, 74)
        self.button_font = pygame.font.Font(None, 36)
        
        self.message = "Welcome"
        self.message_color = Colors.white
        
        self.start_button_text = "Start Game"
        self.exit_button_text = "Exit"
        
        self.start_button_color = Colors.light_blue
        self.exit_button_color = Colors.red
        
        self.start_button_rect = pygame.Rect(self.width // 2 - 100, self.height // 2 - 50, 200, 50)
        self.exit_button_rect = pygame.Rect(self.width // 2 - 100, self.height // 2 + 20, 200, 50)

    def draw(self):
        self.screen.fill(Colors.black)
        
        message_surface = self.font.render(self.message, True, self.message_color)
        message_rect = message_surface.get_rect(center=(self.width // 2, self.height // 3))
        self.screen.blit(message_surface, message_rect)
        
        pygame.draw.rect(self.screen, self.start_button_color, self.start_button_rect)
        pygame.draw.rect(self.screen, self.exit_button_color, self.exit_button_rect)
        
        start_button_surface = self.button_font.render(self.start_button_text, True, (0, 0, 0))
        exit_button_surface = self.button_font.render(self.exit_button_text, True, (0, 0, 0))
        
        start_button_rect = start_button_surface.get_rect(center=self.start_button_rect.center)
        exit_button_rect = exit_button_surface.get_rect(center=self.exit_button_rect.center)
        
        self.screen.blit(start_button_surface, start_button_rect)
        self.screen.blit(exit_button_surface, exit_button_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button_rect.collidepoint(event.pos):
                return "start"
            elif self.exit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

