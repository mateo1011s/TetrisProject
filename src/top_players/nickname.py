import pygame
from src.colors.colors import Colors

class NicknameWindow:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.title_font = pygame.font.Font(None, 48)
        self.subtitle_font = pygame.font.Font(None, 24)
        self.input_font = pygame.font.Font(None, 36)
        self.button_font = pygame.font.Font(None, 36)
        self.nickname = ""
        self.max_length = 10
        self.input_rect = pygame.Rect((self.width // 2) - 100, (self.height // 2) - 50, 200, 50)
        self.input_active = True
        self.title_text = "Enter your nickname"
        self.subtitle_text = "max 10 characters allowed"
        self.return_button_text = "Return"
        self.return_button_color = Colors.red
        self.return_button_rect = pygame.Rect((self.width // 2)- 100, (self.height // 2) + 50, 200, 50)

    def draw(self):
        self.screen.fill(Colors.black)
        title_surface = self.title_font.render(self.title_text, True, Colors.white)
        title_rect = title_surface.get_rect(center=(self.width // 2, self.height // 2 - 120))
        self.screen.blit(title_surface, title_rect)

        subtitle_surface = self.subtitle_font.render(self.subtitle_text, True, Colors.white)
        subtitle_rect = subtitle_surface.get_rect(center=(self.width // 2, self.height // 2 - 80))
        self.screen.blit(subtitle_surface, subtitle_rect)

        pygame.draw.rect(self.screen, Colors.white, self.input_rect, 2)
        input_text = self.nickname
        input_surface = self.input_font.render(input_text, True, Colors.white)
        input_rect = input_surface.get_rect(center=self.input_rect.center)
        self.screen.blit(input_surface, input_rect)

        pygame.draw.rect(self.screen, self.return_button_color, self.return_button_rect)
        return_button_surface = self.button_font.render(self.return_button_text, True, Colors.black)
        return_button_rect = return_button_surface.get_rect(center=self.return_button_rect.center)
        self.screen.blit(return_button_surface, return_button_rect)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and self.input_active:
            if event.key == pygame.K_BACKSPACE:
                self.nickname = self.nickname[:-1]
            elif len(self.nickname) < self.max_length and event.unicode.isprintable():
                self.nickname += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.return_button_rect.collidepoint(event.pos):
                return "main_menu"
            if self.input_rect.collidepoint(event.pos):
                self.input_active = True
            else:
                self.input_active = False

    def reset(self):
        self.nickname = ""
        self.input_active = True