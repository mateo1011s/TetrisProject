import pygame,sys
from src.colors.colors import Colors

class PauseWindow:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pygame.font.Font(None, 74)
        self.button_font = pygame.font.Font(None, 36)

        self.message = "Paused"
        self.message_color = Colors.white
        
        self.resume_button_text = "Resume"
        self.main_menu_button_text = "Main Menu"
        self.restart_button_text = "Restart"
        self.exit_button_text = "Exit"
        
        self.resume_button_color = Colors.purple
        self.main_menu_button_color = Colors.turquoise
        self.restart_button_color = Colors.green
        self.exit_button_color = Colors.red
        
        self.resume_button_rect = pygame.Rect((self.width // 2) - 100, (self.height // 2) - 90, 200, 50)
        self.main_menu_button_rect = pygame.Rect((self.width // 2) - 100, (self.height // 2) - 20, 200, 50)
        self.restart_button_rect = pygame.Rect((self.width // 2) - 100, (self.height // 2) + 50, 200, 50)
        self.exit_button_rect = pygame.Rect((self.width // 2)- 100, (self.height // 2) + 120, 200, 50)
        
    def draw(self):
        self.screen.fill(Colors.black)
        
        message_surface = self.font.render(self.message, True, self.message_color)
        message_rect = message_surface.get_rect(center=(self.width // 2, self.height // 3 - 40))
        self.screen.blit(message_surface, message_rect)
        
        pygame.draw.rect(self.screen, self.resume_button_color, self.resume_button_rect)
        pygame.draw.rect(self.screen, self.main_menu_button_color, self.main_menu_button_rect)
        pygame.draw.rect(self.screen, self.restart_button_color, self.restart_button_rect)
        pygame.draw.rect(self.screen, self.exit_button_color, self.exit_button_rect)
        
        resume_button_surface = self.button_font.render(self.resume_button_text, True, Colors.black)
        main_menu_button_surface = self.button_font.render(self.main_menu_button_text, True, Colors.black)
        restart_button_surface = self.button_font.render(self.restart_button_text, True, Colors.black)
        exit_button_surface = self.button_font.render(self.exit_button_text, True, Colors.black)
        
        resume_button_rect = resume_button_surface.get_rect(center=self.resume_button_rect.center)
        main_menu_button_rect = main_menu_button_surface.get_rect(center=self.main_menu_button_rect.center)
        restart_button_rect = restart_button_surface.get_rect(center=self.restart_button_rect.center)
        exit_button_rect = exit_button_surface.get_rect(center=self.exit_button_rect.center)
        
        self.screen.blit(resume_button_surface, resume_button_rect)
        self.screen.blit(main_menu_button_surface, main_menu_button_rect)
        self.screen.blit(restart_button_surface, restart_button_rect)
        self.screen.blit(exit_button_surface, exit_button_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.resume_button_rect.collidepoint(event.pos):
                return "resume" 
            elif self.main_menu_button_rect.collidepoint(event.pos):
                return "main_menu"
            elif self.restart_button_rect.collidepoint(event.pos):
                return "restart"
            elif self.exit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
