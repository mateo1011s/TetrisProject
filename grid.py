import pygame

class Grid:
    def __init__(self):
        self.num_rows = 20 
        self.num_columns = 10
        self.cell_size= 30
        self.grid = [[0 for j in range(self.num_columns) ] for i in range (self.num_rows)]
        self.colors = self.get_cell_colors()

    def print_grid(self):
        for row in range (self.num_rows):
            for columns in range (self.num_columns):
                print(self.grid[row][columns], end = " " )
            print()

    def get_cell_colors(self):
        dark_gray = (26,31,40)
        green = (47,230,23)
        red = (232,18,18)
        orange = (226,116,17)
        yellow = (237,234,4)
        purple = (166,0,247)
        cyan = (21,204,209)
        blue = (13,64,216)

        return[dark_gray,green,red,orange,yellow,purple,cyan,blue]
    
    def draw(self, screen):
        for row in range(self.num_rows):
            for columns in range(self.num_columns):
                cell_value = self.grid[row][columns]
                cell_rect = pygame.Rect(columns*self.cell_size+1, row*self.cell_size+1,
                self.cellSize-1,self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cell_value],cell_rect)