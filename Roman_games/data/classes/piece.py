import pygame

class Piece:
    def __init__(self, pos, color, board):
    
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.has_moved = False
        
    def get_moves(self,board):
        output = []
        for direction in self.get_possible_moves(board):
            for square in direction:
                if square.occupying_piece is not None:
                    break

                else:
                    output.append(square)
        return output
    
    #returns available moves
    def get_valid_moves(self,board):
        output = []
        
        for square in self.get_moves(board):
            output.append(square)
        return output

    #handles every move
    def move(self, board, square, force=False):
        for i in board.squares:
            i.highlight = False
            
        if square in self.get_valid_moves(board) or force:
            prev_square = board.get_square_from_pos(self.pos)
            self.pos,self.x,self.y = square.pos,square.x,square.y
            prev_square.occupying_piece = None
            square.occupying_piece = self
            board.selected_piece = None
            self.has_moved = True
            return True
            
        elif board.trap_piece is not None:
            prev_square = board.get_square_from_pos(self.pos)
            self.pos,self.x,self.y = square.pos,square.x,square.y
            prev_square.occupying_piece = None
            square.occupying_piece = None
            board.selected_piece = None
            self.has_moved = True
            if self.color =='white':
                board.black_counter +=1
            else:
                board.white_counter +=1
            return True
             
        else:
            board.selected_piece = None
            return False
            

    def attacking_squares(self, board):
        return self.get_moves(board)
