import pygame,sys
from src.colors.colors import Colors

class GameOverWindow:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pygame.font.Font(None, 74)
        self.button_font = pygame.font.Font(None, 36)
        self.water_mark_font = pygame.font.Font(None, 24)
        
        self.message = "Game Over"
        self.message_color = Colors.white
        self.water_mark = "Abby<3"
        self.water_mark_color = Colors.dark_black
        
        self.main_menu_button_text = "Main Menu"
        self.restart_button_text = "Restart"
        self.exit_button_text = "Exit"
        
        self.main_menu_button_color = Colors.turquoise
        self.restart_button_color = Colors.green
        self.exit_button_color = Colors.red
        
        self.main_menu_button_rect = pygame.Rect((self.width // 2) - 100, (self.height // 2) - 70, 200, 50)
        self.restart_button_rect = pygame.Rect((self.width // 2) - 100, (self.height // 2), 200, 50)
        self.exit_button_rect = pygame.Rect((self.width // 2)- 100, (self.height // 2) + 70, 200, 50)
        
    def draw(self):
        self.screen.fill(Colors.black)
        
        message_surface = self.font.render(self.message, True, self.message_color)
        message_rect = message_surface.get_rect(center=(self.width // 2, self.height // 3))
        self.screen.blit(message_surface, message_rect)

        water_mark_surface = self.water_mark_font.render(self.water_mark, True, self.water_mark_color)
        water_mark_rect = water_mark_surface.get_rect(center= (50,600))
        self.screen.blit(water_mark_surface, water_mark_rect)
        
        pygame.draw.rect(self.screen, self.main_menu_button_color, self.main_menu_button_rect)
        pygame.draw.rect(self.screen, self.restart_button_color, self.restart_button_rect)
        pygame.draw.rect(self.screen, self.exit_button_color, self.exit_button_rect)
        
        main_menu_button_surface = self.button_font.render(self.main_menu_button_text, True, Colors.black)
        restart_button_surface = self.button_font.render(self.restart_button_text, True, Colors.black)
        exit_button_surface = self.button_font.render(self.exit_button_text, True, Colors.black)
        
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
