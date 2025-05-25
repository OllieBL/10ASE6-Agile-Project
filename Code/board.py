import pygame
from pygame.locals import *
from sys import exit
import combat_objects


# the board class for combat to take place on. it just creates the board and stores the locations and id's of objects on the board for the combat functions to take place
class CombatBoard:
    def __init__(self, combat_objects, board_dimensions, screen):
        self._combat_objects = combat_objects
        self._board_dimensions = board_dimensions
        self._board_tiles = []
        self.screen = screen

        self.create_board()
        self.display_board()
    
    def create_board(self):
        for i in range(self._board_dimensions[0]):
            self._board_tiles.append([])
            for j in range(self._board_dimensions[1]):
                self._board_tiles[i].append(Tile(False))

    def display_board(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()


            for i in range(len(self._board_tiles)):
                for j in range(len(self._board_tiles[i])):
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((i*35+10), (j*35+10), 30, 30))
            pygame.display.flip()
                    





class Tile:
    def __init__(self, combat_object):
        self._combat_object = combat_object

    def get_combat_object(self):
        return self._combat_object
    
    def set_combat_object(self, combat_object):
        self._combat_object = combat_object


pygame.init()

screen = pygame.display.set_mode((500, 500))

board = CombatBoard([], [20, 20], screen)