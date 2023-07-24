from colors import Colors
import pygame
from position import Position

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, row, column):
        self.row_offset += row
        self.column_offset += column

    def get_cell_positions(self):
        tiles =self.cells[self.rotation_state]
        move_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            move_tiles.append(position)
        return move_tiles
    
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotate(self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1


    def draw(self, screen):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(
                tile.column * self.cell_size + 1,
                tile.row * self.cell_size + 1,
                self.cell_size - 1,
                self.cell_size - 1
            )
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
