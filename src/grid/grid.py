import pygame
from src.colors.colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20 
        self.num_columns = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_columns) ] for i in range (self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range (self.num_rows):
            for columns in range (self.num_columns):
                print(self.grid[row][columns], end = " " )
            print()
    
    def is_inside(self,row,column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_columns:
            return True 
        return False

    def draw(self, screen):
        for row in range(self.num_rows):
            for columns in range(self.num_columns):
                cell_value = self.grid[row][columns]
                cell_rect = pygame.Rect(columns*self.cell_size+1, row*self.cell_size+1,
                self.cell_size-1,self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cell_value],cell_rect)