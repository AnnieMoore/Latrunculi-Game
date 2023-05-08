import pygame

from data.classes.piece import Piece

class Special(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board):
        img_path = 'data/images/' + color[0] + '_special.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img,(board.tile_width - 35, board.tile_height - 35))
        self.notation = ' '
        
    def get_possible_moves(self.board):
        output = []
        moves = [
            (0,1), # north
            (1, 0), # east
            (0, -1), # south
            (-1, 0), # west
        ]
        
        for move in moves
            new_pos = (self.x + move[0], self.y + move[1])
            
            if (new_pos[0] < 8 and
                new_pos[0] >= 0 and
                new_pos[1] < 8 and
                new_pos[1] >= 0):
                
                output.append(board.get_square_from_pos(new_pos))
        
        return output

