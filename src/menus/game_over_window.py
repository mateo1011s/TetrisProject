import pygame
import sys

class GameOverWindow:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pygame.font.Font(None, 74)
        self.button_font = pygame.font.Font(None, 36)
        
        self.message = "Game Over"
        self.message_color = (255, 255, 255)
        
        self.main_menu_button_text = "Main Menu"
        self.restart_button_text = "Restart"
        self.exit_button_text = "Exit"
        
        self.main_menu_button_color = (0, 255, 0)
        self.restart_button_color = (0, 0, 255)
        self.exit_button_color = (255, 0, 0)
        
        self.main_menu_button_rect = pygame.Rect(self.width // 2 - 100, self.height // 2 - 70, 200, 50)
        self.restart_button_rect = pygame.Rect(self.width // 2 - 100, self.height // 2, 200, 50)
        self.exit_button_rect = pygame.Rect(self.width // 2 - 100, self.height // 2 + 70, 200, 50)
        
    def draw(self):
        self.screen.fill((0,0,0))
        
        message_surface = self.font.render(self.message, True, self.message_color)
        message_rect = message_surface.get_rect(center=(self.width // 2, self.height // 3))
        self.screen.blit(message_surface, message_rect)
        
        pygame.draw.rect(self.screen, self.main_menu_button_color, self.main_menu_button_rect)
        pygame.draw.rect(self.screen, self.restart_button_color, self.restart_button_rect)
        pygame.draw.rect(self.screen, self.exit_button_color, self.exit_button_rect)
        
        main_menu_button_surface = self.button_font.render(self.main_menu_button_text, True, (0, 0, 0))
        restart_button_surface = self.button_font.render(self.restart_button_text, True, (0, 0, 0))
        exit_button_surface = self.button_font.render(self.exit_button_text, True, (0, 0, 0))
        
        main_menu_button_rect = main_menu_button_surface.get_rect(center=self.main_menu_button_rect.center)
        restart_button_rect = restart_button_surface.get_rect(center=self.restart_button_rect.center)
        exit_button_rect = exit_button_surface.get_rect(center=self.exit_button_rect.center)
        
        self.screen.blit(main_menu_button_surface, main_menu_button_rect)
        self.screen.blit(restart_button_surface, restart_button_rect)
        self.screen.blit(exit_button_surface, exit_button_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.main_menu_button_rect.collidepoint(event.pos):
                return "main_menu"
            elif self.restart_button_rect.collidepoint(event.pos):
                return "restart"
            elif self.exit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
