import pygame,sys
from src.game.interface_user import InterfaceUser

class EventsInGame:
    def __init__(self, screen):
        self.GAME_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.GAME_UPDATE, 600)
        self.interface = InterfaceUser(screen)
        self.game = self.interface.game

    
    def process_events(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.game.show_welcome:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    action = self.game.welcome_window.handle_event(event)
                    if action == "start":
                        self.game.show_welcome = False
            elif self.game.show_game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    action = self.game.game_over_window.handle_event(event)
                    if action == "main_menu":
                        self.game.show_welcome = True
                        self.game.show_game_over = False
                        self.interface.reset_game()
                    elif action == "restart":
                        self.game.show_game_over = False
                        self.game.reset()
            else: 
                if event.type == pygame.KEYDOWN:
                    if self.game.game_over:
                        self.game.show_game_over = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a and self.game.game_over == False:
                        self.game.move_left()
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d and self.game.game_over == False:
                        self.game.move_right()
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s and self.game.game_over == False:
                        self.game.move_down()
                        self.game.update_score(0, 1)
                    if event.key == pygame.K_UP or event.key == pygame.K_w and self.game.game_over == False:
                        self.game.rotate()
                if event.type == self.GAME_UPDATE and self.game.game_over == False:
                    self.game.move_down()
        if self.game.show_welcome:
            self.game.welcome_window.draw()
        elif self.game.show_game_over:
            self.game.game_over_window.draw()
        else:
            self.interface.draw(screen)
            self.game.draw(screen)    