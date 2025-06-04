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
        self._image_list = []
        self.screen = screen
        self._tick = 0

        self.create_board()
        self.load_images()
        self.display_board()
    
    def create_board(self):
        for i in range(self._board_dimensions[0]):
            self._board_tiles.append([])

            for j in range(self._board_dimensions[1]):

                self._board_tiles[i].append(Tile(False))

                for x in self._combat_objects:
                    if x.get_board_position() == [i, j]:
                        self._board_tiles[i][j] = Tile(x)
                    

                

    def load_images(self):
        self._image_list = []

        for i in range(len(self._board_tiles)):
            self._image_list.append([])
            
            for j in range(len(self._board_tiles[i])):
                if self._board_tiles[i][j].get_combat_object() != False:
                    tile_image = pygame.image.load(self._board_tiles[i][j].get_combat_object().get_image()).convert()
                    tile_image = pygame.transform.scale(tile_image, (30, 30))

                else:
                    tile_image = False


                self._image_list[i].append(tile_image)

    def display_board(self):
        while True:
            self._tick += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                test = self.update_board(event)

                if test == True:
                    self.load_images()


            for i in range(len(self._board_tiles)):
                for j in range(len(self._board_tiles[i])):
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect((i*35+10), (j*35+10), 30, 30))
                    if self._image_list[i][j] != False:
                        self.screen.blit(self._image_list[i][j], (i*35+10, j*35+10))
            

            pygame.display.flip()

    def update_board(self, event):
        if event.type == KEYDOWN:
            current_position = []
            enemy_new_position = ['']
            for i in self._combat_objects:
                current_position.append([i.get_board_position()[0], i.get_board_position()[1]])

            for i in range(len(self._combat_objects) - 1):
                enemy_new_position.append('')

            if event.key == K_LEFT and current_position[0][0] > 0:
                self._combat_objects[0].set_board_position([current_position[0][0] - 1, current_position[0][1]])
                new_position = [current_position[0][0] - 1, current_position[0][1]]
                print('went left')

            elif event.key == K_RIGHT and current_position[0][0] < (self._board_dimensions[0] - 1):
                self._combat_objects[0].set_board_position([current_position[0][0] + 1, current_position[0][1]])
                new_position = [current_position[0][0] + 1, current_position[0][1]]
                print('went right')

            elif event.key == K_UP and current_position[0][1] > 0:
                self._combat_objects[0].set_board_position([current_position[0][0], current_position[0][1] - 1])
                new_position = [current_position[0][0], current_position[0][1] - 1]
                print('went up')

            elif event.key == K_DOWN and current_position[0][1] < (self._board_dimensions[1] - 1):
                self._combat_objects[0].set_board_position([current_position[0][0], current_position[0][1] + 1])
                new_position = [current_position[0][0], current_position[0][1] + 1]
                print('went right')

            else:
                new_position = current_position[0]
            
            for i in range(len(self._combat_objects) - 1):
                if self._tick % 2 == 0:
                
                    enemy_new_position[i] = self._combat_objects[i+1].decide_movement(self._combat_objects[0].get_board_position())
                    self._board_tiles[current_position[i+1][0]][current_position[i+1][1]] = Tile(False)
                    self._board_tiles[enemy_new_position[i][0]][enemy_new_position[i][1]] = Tile(self._combat_objects[i+1])


            
            self._board_tiles[current_position[0][0]][current_position[0][1]] = Tile(False)
            self._board_tiles[new_position[0]][new_position[1]] = Tile(self._combat_objects[0])
            
            return True



class Tile:
    def __init__(self, combat_object):
        self._combat_object = combat_object

    def get_combat_object(self):
        return self._combat_object
    
    def set_combat_object(self, combat_object):
        self._combat_object = combat_object