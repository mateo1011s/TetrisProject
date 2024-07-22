import pygame
from src.grid.grid import Grid
from src.blocks.blocks import *
from src.menus.welcome_window import WelcomeWindow
from src.menus.game_over_window import GameOverWindow
from src.menus.pause_window import PauseWindow
from src.top_players.scores import ScoresWindow
from src.top_players.nickname import NicknameWindow
from src.database.db import save_score
import random

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.grid = Grid()
        self.blocks = [Lblock(), Jblock(), Iblock(), Oblock(), Sblock(), Tblock(), Zblock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.show_welcome = True
        self.show_nickname = False
        self.show_game_over = False
        self.show_pause = False
        self.show_scores = False
        self.welcome_window = WelcomeWindow(screen)
        self.nickname_window = NicknameWindow(screen)
        self.player_nickname = ""
        self.game_over_window = GameOverWindow(screen) 
        self.pause_window = PauseWindow(screen)
        self.scores_window = ScoresWindow(screen)
        self.score = 0
        self.GAME_UPDATE = pygame.USEREVENT
        self.initial_speed = 600
        self.min_speed = 50
        self.current_speed = self.initial_speed

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 200
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points
        self.speed_game()
    
    def speed_game(self):
        score_for_speed_increase = 100
        speed_decrement = 50
        new_speed = self.initial_speed - ((self.score // score_for_speed_increase) * speed_decrement)
        self.current_speed = max(new_speed, self.min_speed)
        pygame.time.set_timer(self.GAME_UPDATE, self.current_speed)

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [Lblock(), Jblock(), Iblock(), Oblock(), Sblock(), Tblock(), Zblock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        self.current_block.move(0,-1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,1)

    def move_right(self):
        self.current_block.move(0,1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,-1)
    
    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1,0)
            self.lock_block()
    
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.update_score(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True
            save_score(self.score)

    def reset(self):
        self.grid.reset()
        self.blocks = [Lblock(), Jblock(), Iblock(), Oblock(), Sblock(), Tblock(), Zblock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        self.game_over = False
        self.current_speed = self.initial_speed
        pygame.time.set_timer(self.GAME_UPDATE, self.initial_speed)

    def reset_game(self):
        self.reset()
        self.welcome_window = WelcomeWindow(self.screen)
        self.game_over_window = GameOverWindow(self.screen)
        self.pause_window = PauseWindow(self.screen)
        self.scores_window = ScoresWindow(self.screen)
        self.show_welcome = True
        self.show_nickname = False
        self.show_game_over = False
        self.show_pause = False
        self.show_scores = False
        self.current_speed = self.initial_speed
        pygame.time.set_timer(self.GAME_UPDATE, self.initial_speed)


    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
    
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        if self.next_block.id == 4:
            self.next_block.draw(screen, 255, 395)
        elif self.next_block.id == 3: 
            self.next_block.draw(screen, 257, 410)
        else:
            self.next_block.draw(screen, 270, 390)