import pygame
from pygame.locals import *
from sys import exit


# the board class for combat to take place on. it just creates the board and stores the locations and id's of objects on the board for the combat functions to take place
class CombatBoard:
    def __init__(self, combat_objects, board_dimensions, screen):
        self._combat_objects = combat_objects
        self._board_dimensions = board_dimensions
        self._board_tiles = []
        self._image_list = []
        self.screen = screen
        self._tick = 0
        self._combat_over = False
        self._attacking = False

        self.create_board()
        self.load_images()
    
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
                    tile_image = pygame.image.load(self._board_tiles[i][j].get_combat_object().get_image()).convert_alpha()
                    tile_image = pygame.transform.scale(tile_image, (30, 30))

                else:
                    tile_image = False


                self._image_list[i].append(tile_image)

    def display_board(self):
        self.screen.fill((0, 0, 0))
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                test = self.update_board(event)

                if test == True:
                    self.load_images()


            for i in range(len(self._board_tiles)):
                for j in range(len(self._board_tiles[i])):
                    pygame.draw.rect(self.screen, (255, 255, 255), Rect((i*35+10), (j*35+10), 30, 30))
                    if self._image_list[i][j] != False:
                        self.screen.blit(self._image_list[i][j], (i*35+10, j*35+10))
            

            pygame.display.flip()

    def update_board(self, event):
        if event.type == KEYDOWN:
            current_position = []
            enemy_current_position = []
            enemy_new_position = []
            moved = False
            change = False
            for i in self._combat_objects:
                current_position.append([i.get_board_position()[0], i.get_board_position()[1]])
                if i.get_health() <= 0:
                    self._combat_objects[self._combat_objects.index(i)]

            for i in range(len(self._combat_objects) - 1):
                enemy_new_position.append('')
                enemy_current_position.append(self._combat_objects[i+1].get_board_position())

            if event.key == K_LEFT and current_position[0][0] > 0 and self._attacking == False:
                self._combat_objects[0].set_board_position([current_position[0][0] - 1, current_position[0][1]])
                new_position = [current_position[0][0] - 1, current_position[0][1]]
                moved = True
                change = True

            elif event.key == K_RIGHT and current_position[0][0] < (self._board_dimensions[0] - 1) and self._attacking == False:
                self._combat_objects[0].set_board_position([current_position[0][0] + 1, current_position[0][1]])
                new_position = [current_position[0][0] + 1, current_position[0][1]]
                moved = True
                change = True

            elif event.key == K_UP and current_position[0][1] > 0 and self._attacking == False:
                self._combat_objects[0].set_board_position([current_position[0][0], current_position[0][1] - 1])
                new_position = [current_position[0][0], current_position[0][1] - 1]
                moved = True
                change = True

            elif event.key == K_DOWN and current_position[0][1] < (self._board_dimensions[1] - 1) and self._attacking == False:
                self._combat_objects[0].set_board_position([current_position[0][0], current_position[0][1] + 1])
                new_position = [current_position[0][0], current_position[0][1] + 1]
                moved = True
                change = True

            else:
                new_position = current_position[0]

            if event.key == K_a and self._attacking == False:
                self._attacking = True
            elif event.key == K_a and self._attacking == True:
                self._attacking = False

            if event.key == K_RIGHT and self._attacking == True:
                self._combat_objects[0].attack(0, self._combat_objects)
                self._attacking = False
                change = True
            if event.key == K_DOWN and self._attacking == True:
                self._combat_objects[0].attack(1, self._combat_objects)
                self._attacking = False
                change = True
            if event.key == K_LEFT and self._attacking == True:
                self._combat_objects[0].attack(2, self._combat_objects)
                self._attacking = False
                change = True
            if event.key == K_UP and self._attacking == True:
                self._combat_objects[0].attack(3, self._combat_objects)
                self._attacking = False
                change = True
            
            if change == True:
                checker = 0
                for i in range(len(self._combat_objects) - 1):
                    test = False
                    if self._combat_objects[i+1-checker].get_health() <= 0:
                        self._combat_objects.pop(i+1-checker)
                        test = True
                    if self._tick % 2 == 0:

                        enemy_new_position[i] = self._combat_objects[i+1-checker].decide_movement(self._combat_objects[0].get_board_position(), enemy_current_position)
                        enemy_current_position[i] = enemy_new_position[i]
                        self._board_tiles[current_position[i+1][0]][current_position[i+1][1]] = Tile(False)
                        self._board_tiles[enemy_new_position[i][0]][enemy_new_position[i][1]] = Tile(self._combat_objects[i+1-checker])
                        
                    if test == True:
                        checker +=1
                    
                self._tick += 1


                if moved == True:
                    self._board_tiles[current_position[0][0]][current_position[0][1]] = Tile(False)
                    self._board_tiles[new_position[0]][new_position[1]] = Tile(self._combat_objects[0])
            
            return True
        
    def check_combat_complete(self):
        if self._combat_objects[0].get_health() == 0:
            self._combat_over = True
        else:
            enemy_health_sum = 0
            for i in range(len(self._combat_objects) - 1):
                enemy_health_sum += self._combat_objects[i + 1].get_health()
            if enemy_health_sum == 0:
                self._combat_over = True



class Tile:
    def __init__(self, combat_object):
        self._combat_object = combat_object

    def get_combat_object(self):
        return self._combat_object
    
    def set_combat_object(self, combat_object):
        self._combat_object = combat_object