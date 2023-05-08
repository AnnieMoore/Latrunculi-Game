import pygame

#creates tiles

class Square:
    def __init__(self, x, y, width, height):
    
        #represents the rows
        self.x = x
        #represents the columns
        self.y = y
        #this is the width of a square
        self.width = width
        #this is the height of a square
        self.height = height
        
        #these dictate where the chess tile is drawn in the window
        self.abs_x = x*width
        self.abs_y = y*height
        #gives the full tile position
        self.abs_pos = (self.abs_x, self.abs_y)
        
        #gives the row and column number
        self.pos = (x,y)
        
        #determines if the square should be light or dark and defines those colors
        self.color = 'light' if (x+y)%2 == 0 else 'dark'
        self.draw_color = (220, 208, 194) if self.color == 'light' else (53, 53, 53)
        #will highlight the tiles with the possible movement of selected piece
        self.highlight_color = (100, 249, 83) if self.color == 'light' else (0, 228, 10)
        self.occupying_piece = None
        
        self.coord = self.get_coord()
        
        self.highlight = False
        
        #configures the width, height, and loctation of a tile
        self.rect = pygame.Rect(self.abs_x, self.abs_y, self.width, self.height)
        
        #this will be the formal notation of the tiles
    def get_coord(self):
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y + 1)
            
    #configures the board
    def draw(self, display):
        # configures if tile should be light or dark or highlighted tile
        if self.highlight:
            pygame.draw.rect(display, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(display, self.draw_color, self.rect)
        # adds the piece icons, will try to randomize later
        if self.occupying_piece != None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)
        
