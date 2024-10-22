import pygame,sys
from src.game.interface_user import InterfaceUser

class EventsInGame:
    def __init__(self, screen):
        self.interface = InterfaceUser(screen)
        self.game = self.interface.game
        pygame.time.set_timer(self.game.GAME_UPDATE, self.game.initial_speed)

    
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
                        self.game.show_nickname = True 
                    if action == "scores":
                        self.game.show_scores = True
                        self.game.show_welcome = False
            elif self.game.show_nickname:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    action = self.game.nickname_window.handle_event(event)
                    if action == "main_menu":
                        self.game.show_welcome = True
                        self.game.show_nickname = False
                        self.game.nickname_window.reset()
                self.game.nickname_window.handle_event(event)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.game.player_nickname = self.game.nickname_window.nickname
                    self.game.show_nickname = False
                    self.game.reset()
            elif self.game.show_game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    action = self.game.game_over_window.handle_event(event)
                    if action == "main_menu":
                        self.game.show_welcome = True
                        self.game.show_game_over = False
                        self.interface.reset_game()
                        self.game.nickname_window.reset()
                    if action == "scores":
                        self.game.show_scores = True
                        self.game.show_game_over = False
                    elif action == "restart":
                        self.game.show_game_over = False
                        self.game.reset()
            elif self.game.show_scores:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    action = self.game.scores_window.handle_event(event)
                    if action == "main_menu":
                        self.game.show_welcome = True
                        self.game.show_scores = False
                        self.interface.reset_game()
                        self.game.nickname_window.reset()
            elif self.game.show_pause:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    action = self.game.pause_window.handle_event(event)
                    if action == "resume":
                        self.game.show_pause = False
                    elif action == "main_menu":
                        self.game.show_welcome = True
                        self.game.show_pause = False
                        self.interface.reset_game()
                        self.game.nickname_window.reset()
                    elif action == "restart":
                        self.game.show_pause = False
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
                    if event.key == pygame.K_ESCAPE:
                        self.game.show_pause = True
                if event.type == self.game.GAME_UPDATE and self.game.game_over == False:
                    self.game.move_down()
        if self.game.show_welcome:
            self.game.welcome_window.draw()
        elif self.game.show_nickname:
            self.game.nickname_window.draw()
        elif self.game.show_game_over:
            self.game.game_over_window.draw()
        elif self.game.show_pause:
            self.game.pause_window.draw()
        elif self.game.show_scores:
            self.game.scores_window.draw()
        else:
            self.interface.draw(screen)
            self.game.draw(screen)    