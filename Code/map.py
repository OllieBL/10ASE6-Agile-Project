import pygame
from pygame.locals import *
from sys import exit

class Map:
    def __init__(self, room_quantity, screen_dimensions, screen):
        self._room_quantity = room_quantity
        self._rooms = []
        self._screen_dimensions = screen_dimensions
        self.screen = screen
        
        self.createMap()


    def createMap(self):
        for column in range(self._room_quantity):
            row = 0
            while row <= column:
                column -= row
                row += 1
            
            self._rooms.append(Room([row, column], 0, 0))

        self._rooms.append(Room([row+2, (row+1)/2], 0, 0))


    def display_map(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            for i in self._rooms:
                i_room_id = i.get_room_id()
                coord_calculator = lambda a, b, c : (a / 2) - (b * 50) + (c * 100)

                room_coordinate = coord_calculator(self._screen_dimensions[0], i_room_id[0], i_room_id[1])

                pygame.draw.circle(
                    self.screen, 
                    (255, 255, 255), 
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

            pygame.display.flip()
                


class Room:
    def __init__(self, room_id, layout, combat_objects):
        self._room_id = room_id
        self._layout = layout
        self._combat_objects = combat_objects

    def get_room_id(self):
        return self._room_id





pygame.init()

screen = pygame.display.set_mode((1920, 1080))

map = Map(10, [1920, 1080], screen)
map.display_map()