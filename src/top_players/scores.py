from src.colors.colors import Colors
import pygame 

class ScoresWindow:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.resume_button_text = "Go Main Menu"
        self.button_font = pygame.font.Font(None, 36)
        self.resume_button_color = Colors.orange
        self.resume_button_rect = pygame.Rect((self.width // 2)- 100, (self.height // 2) + 90, 200, 50)

    def draw(self):
        self.screen.fill(Colors.black)
        pygame.draw.rect(self.screen, self.resume_button_color, self.resume_button_rect)
        resume_button_surface = self.button_font.render(self.resume_button_text, True, Colors.black)
        resume_button_rect = resume_button_surface.get_rect(center=self.resume_button_rect.center)
        self.screen.blit(resume_button_surface, resume_button_rect)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.resume_button_rect.collidepoint(event.pos):
                return "main_menu"
