import pygame

from data.classes.square import Square
from data.classes.pieces.Basic import Basic


# Game state checker

class Board:
    def __init__(self, width, height):
    
        self.width = width
        self.height = height
        
        #divide the board into 64 equal squares
        self.tile_width = width // 8
        self.tile_height = height//7
        self.selected_piece = None
        
        #used to keep score
        self.white_counter=0
        self.black_counter=0
        
        #decides who will go first
        self.turn = 'white'
        
        #generates 2D board. Will make empty as we want to add pieces later
        self.config = [
            ['wC', 'wC', 'wC', 'wC', 'wC', 'wC', 'wC', 'wC'],
            ['wC', 'wC', 'wC', 'wC', 'wC', 'wC', 'wC', 'wC'],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['bC','bC','bC','bC','bC','bC','bC','bC'],
            ['bC', 'bC', 'bC', 'bC', 'bC', 'bC', 'bC', 'bC'],
            ]
            
        self.squares = self.generate_squares()
        
        self.setup_board()
        
    #makes the tiles (position, color) and puts them in a list
    def generate_squares(self):
        #array to hold information for board
        output = []
        for y in range(8):
            for x in range(8):
                output.append(Square(x,y,self.tile_width,self.tile_height))
        
        return output
      
    #goes through each square generated in generate_squares and pulls the one that we need to modify
    def get_square_from_pos(self,pos):
        for square in self.squares:
            if (square.x, square.y) == (pos[0],pos[1]):
                return square
                
    #shows what piece is on a given square
    def get_piece_from_pos(self,pos):
        return self.get_square_from_pos(pos).occupying_piece
    
    #identifies shape and color of each piece on board
    def setup_board(self):
        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
                if piece != '':
                    square = self.get_square_from_pos((x,y))
                    if piece[1] == 'C':
                        square.occupying_piece = Basic((x,y), 'white' if piece[0] == 'w' else 'black', self)
    
    def get_color_of_turn(self):
        return self.turn
                    
        
    #this function detects each click in the game
    def handle_click(self, mx, my):
        self.mx = mx
        self.my = my
        x = self.mx // self.tile_width
        y = self.my // self.tile_height
        clicked_square = self.get_square_from_pos((x, y))
        if self.selected_piece is None:
            if clicked_square.occupying_piece is not None:
                #if clicked_square.occupying_piece.color == self.turn:
                self.selected_piece = clicked_square.occupying_piece
        elif self.selected_piece.move(self, clicked_square):
            self.turn = 'white' if self.turn == 'black' else 'black'
        elif clicked_square.occupying_piece is not None:
            if clicked_square.occupying_piece.color == self.turn:
                self.selected_piece = clicked_square.occupying_piece


    #highlights all possible moves of a piece once selected
    def draw(self, display):
        if self.selected_piece is not None:
            self.get_square_from_pos(self.selected_piece.pos).highlight = True
            if self.selected_piece.color == self.turn:
                for square in self.selected_piece.get_valid_moves(self):
                    square.highlight = True
        for square in self.squares:
            square.draw(display)
            
    def trap_piece(self):
        output = []
        if self.selected_piece.color != self.turn:
            square = self.get_square_from_pos((self.mx,self.my))
            top = self.get_square_from_pos((self.mx,self.my + 1))
            bottom = self.get_square_from_pos((self.mx,self.my - 1))
            left = self.get_square_from_pos((self.mx - 1,self.my))
            right = self.get_square_from_pos((self.mx + 1,self.my))
            
            if top.occupying_piece.color != self.selected_piece.color and bottom.occupying_piece.color != self.selected_piece.color:
                output = True
                if self.selected_piece.color != 'white':
                    self.white_counter +=1
                else:
                    self.black_counter +=1
            elif left.occupying_piece.color != self.selected_piece.color and right.occupying_piece.color != self.selected_piece.color:
                output = True
                if self.selected_piece.color != 'white':
                    self.white_counter +=1
                else:
                    self.black_counter +=1
        return output
        
    def check_white_counters(self):
        output = False
        if self.white_counter > 2:
            output = True
        return output
        
    def check_black_counters(self):
        output = False
        if self.black_counter > 2:
            output = True
        return output
        
            
    
        
