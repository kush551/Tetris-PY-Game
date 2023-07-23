import pygame, sys
from grid import Grid
from blocks import *

pygame.init()
purple = (128,0,128)

screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game_grid = Grid()

block = OBlock() 


game_grid.print_grid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(purple)
    game_grid.draw(screen)
    block.draw(screen)


    pygame.display.update()
    clock.tick(144)