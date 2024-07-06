import pygame

class Grid:
    def __init__(self):
        self.numRows = 20 
        self.numColumns = 10
        self.cellSize= 30
        self.grid = [[0 for j in range(self.numColumns) ] for i in range (self.numRows)]
        self.colors = self.get_cell_colors()

    def print_grid(self):
        for row in range (self.numRows):
            for columns in range (self.numColumns):
                print(self.grid[row][columns], end = " " )
            print()

    def get_cell_colors(self):
        darkGray = (26,31,40)
        green = (47,230,23)
        red = (232,18,18)
        orange = (226,116,17)
        yellow = (237,234,4)
        purple = (166,0,247)
        cyan = (21,204,209)
        blue = (13,64,216)

        return[darkGray,green,red,orange,yellow,purple,cyan,blue]
    
    def draw(self, screen):
        for row in range(self.numRows):
            for columns in range(self.numColumns):
                cell_value = self.grid[row][columns]
                cell_rect = pygame.Rect(columns*self.cellSize+1, row*self.cellSize+1,
                self.cellSize-1,self.cellSize-1)
                pygame.draw.rect(screen, self.colors[cell_value],cell_rect)