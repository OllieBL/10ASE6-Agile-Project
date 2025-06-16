import pygame
from pygame.locals import *
from sys import exit
import random
import math
import combat_objects
import player
import board

class Map:
    def __init__(self, room_quantity, screen_dimensions, screen, player):
        self._room_quantity = room_quantity
        self._rooms = []
        self._screen_dimensions = screen_dimensions
        self.screen = screen
        self.player = player
        
        self.createMap()


    def createMap(self):
        room_type_amount = [random.randrange(math.floor((self._room_quantity - 1) / 6), math.floor((self._room_quantity - 1) / 3)), random.randrange(math.floor((self._room_quantity - 1) / 6), math.floor((self._room_quantity  - 1) / 3))]
        room_type_list = []
        for i in range(len(room_type_amount)):
            for j in range(room_type_amount[i]):
                room_type_list.append(i+1)

        for i in range(self._room_quantity - 1 - len(room_type_list)):
            room_type_list.append(0)
        
        random.shuffle(room_type_list)
            


        for column in range(self._room_quantity):
            row = 0
            room_type = room_type_list[column - 1]
            while row <= column:
                column -= row
                row += 1


            self._rooms.append(Room([row, column], 0, room_type, self.player, self.screen))

        self._rooms.append(Room([row+2, (row+1)/2], 0, self.player, 0, 0))
        self._room_pos_list = [i.get_room_id() for i in self._rooms]


    def display_map(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_buttons()

            for i in self._rooms:
                i_room_id = i.get_room_id()
                coord_calculator = lambda a, b, c : (a / 2) - (b * 50) + (c * 100)

                room_coordinate = coord_calculator(self._screen_dimensions[0], i_room_id[0], i_room_id[1])

                if i_room_id == self.player.get_pos():
                    pygame.draw.circle(
                        self.screen, 
                        (0, 0, 255), 
                        [room_coordinate, self._screen_dimensions[1] - (i_room_id[0] * 100 + 100)], 
                        20
                        )
                elif i.get_room_type() == 0:
                    pygame.draw.circle(
                        self.screen, 
                        (255, 255, 255), 
                        [room_coordinate, self._screen_dimensions[1] - (i_room_id[0] * 100 + 100)], 
                        20
                        )
                elif i.get_room_type() == 1:
                    pygame.draw.circle(
                        self.screen, 
                        (255, 0, 0), 
                        [room_coordinate, self._screen_dimensions[1] - (i_room_id[0] * 100 + 100)], 
                        20
                        )
                elif i.get_room_type() == 2:
                    pygame.draw.circle(
                        self.screen, 
                        (0, 255, 0), 
                        [room_coordinate, self._screen_dimensions[1] - (i_room_id[0] * 100 + 100)], 
                        20
                        )
                if i_room_id[0] > 0 and i_room_id[1] > 0:
                    pygame.draw.line(
                        self.screen, 
                        (255, 255, 255), 
                        [room_coordinate, self._screen_dimensions[1] - (i_room_id[0] * 100 + 100)], 
                        [coord_calculator(self._screen_dimensions[0], i_room_id[0] - 1, i_room_id[1] - 1), self._screen_dimensions[1] - ((i_room_id[0] - 1) * 100 + 100)] 
                        )
                if i_room_id[1] < i_room_id[0] - 1 and i_room_id[0] > 0:
                    pygame.draw.line(
                        self.screen, 
                        (255, 255, 255), 
                        [room_coordinate, self._screen_dimensions[1] - (i_room_id[0] * 100 + 100)], 
                        [coord_calculator(self._screen_dimensions[0], i_room_id[0] + 1, i_room_id[1] + 1), self._screen_dimensions[1] - ((i_room_id[0] - 1) * 100 + 100)] 
                        )
                    
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                pygame.Rect(300, 300, 100, 50)
            )

            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                pygame.Rect(150, 300, 100, 50)
            )

            pygame.display.flip()

    def check_buttons(self):
        mouse_pos = pygame.mouse.get_pos()

        if 300 <= mouse_pos[0] <= 400 and 300 <= mouse_pos[1] <= 350:
            old_player_pos = self.player.get_pos()
            self.player.set_pos([old_player_pos[0] + 1, old_player_pos[1] + 1])
            self._rooms[self._room_pos_list.index(self.player.get_pos())].generate_layout()
            (self._rooms[self._room_pos_list.index(self.player.get_pos())].get_layout()).display_board()
        if 150 <= mouse_pos[0] <= 250 and 300 <= mouse_pos[1] <= 350:
            old_player_pos = self.player.get_pos()
            self.player.set_pos([old_player_pos[0] + 1, old_player_pos[1]])
        

                


class Room:
    def __init__(self, room_id, combat_objects, room_type, player, screen):
        self._room_id = room_id
        self._layout = []
        self._combat_objects = combat_objects
        self._room_type = room_type
        self.screen = screen
        self._player = player

    def get_room_id(self):
        return self._room_id
    
    def get_room_type(self):
        return self._room_type
    
    def get_layout(self):
        return self._layout
    
    def generate_layout(self):
        combat_objects_list = [self._player.get_combat_state()]
        if self._room_type == 2:
            return 2
        if self._room_type == 1:
            enemy_pos_list = []
            number_of_enemies = self._room_id[0] * 3
            for i in range(number_of_enemies):
                while True:
                    random_pos = [random.randrange(0, 20), random.randrange(0, 16)]
                    if random_pos not in enemy_pos_list:
                        combat_objects_list.append(combat_objects.Enemy(10, 2, 1, 0, 'enemy', random_pos, 'Images and other files/enemy_art.png'))
                        break
        else:
            enemy_pos_list = []
            number_of_enemies = self._room_id[0] * 2
            for i in range(number_of_enemies):
                while True:
                    random_pos = [random.randrange(0, 20), random.randrange(0, 16)]
                    if random_pos not in enemy_pos_list:
                        combat_objects_list.append(combat_objects.Enemy(10, 2, 1, 0, 'enemy', random_pos, 'Images and other files/enemy_art.png'))
                        break
        self._layout = board.CombatBoard(combat_objects_list, [20, 20], self.screen)

    
pygame.init()

screen = pygame.display.set_mode((1920, 1080))

player0 = player.Player([1, 0], combat_objects.Player(10, 2, 2, [], 'player', [0,0], 'Images and other files/test_image.png', []))

map0 = Map(21, [1920, 1080], screen, player0)
map0.display_map()