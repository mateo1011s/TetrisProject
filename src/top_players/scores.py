from src.colors.colors import Colors
from src.database.db import *
import pygame 


class ScoresWindow:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.resume_button_text = "Go Main Menu"
        self.button_font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 48)
        self.resume_button_color = Colors.orange
        self.resume_button_rect = pygame.Rect((self.width // 2) - 100, (self.height // 2) + 90, 200, 50)
        initialize_db()  
        self.top_scores = []
    
    def update_scores(self):
        self.top_scores = get_top_scores()
    
    def draw(self):
        self.update_scores()
        self.screen.fill(Colors.black)

        title_text = "Top Scores"
        title_surface = self.title_font.render(title_text, True, Colors.white)
        title_rect = title_surface.get_rect(center=(self.width // 2, self.height // 2 - 150))
        self.screen.blit(title_surface, title_rect)

        y_offset = self.height // 2 - 100
        for index, (nickname, score) in enumerate(self.top_scores):
            rank_text = f"Rank {index + 1}"
            score_text = f"{nickname}: {score}"
            
            rank_surface = self.button_font.render(rank_text, True, Colors.white)
            rank_rect = rank_surface.get_rect(center=(self.width // 2 - 100, y_offset + (index * 50)))
            self.screen.blit(rank_surface, rank_rect)

            score_surface = self.button_font.render(score_text, True, Colors.white)
            score_rect = score_surface.get_rect(center=(self.width // 2 + 100, y_offset + (index * 50)))
            self.screen.blit(score_surface, score_rect)

        pygame.draw.rect(self.screen, self.resume_button_color, self.resume_button_rect)
        resume_button_surface = self.button_font.render(self.resume_button_text, True, Colors.black)
        resume_button_rect = resume_button_surface.get_rect(center=self.resume_button_rect.center)
        self.screen.blit(resume_button_surface, resume_button_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.resume_button_rect.collidepoint(event.pos):
                return "main_menu"