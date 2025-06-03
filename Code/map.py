import pygame
from pygame.locals import *
from sys import exit

class Map:
    def __init__(self, rooms, screen_dimensions, screen):
        self._rooms = rooms
        self._screen_dimensions = screen_dimensions
        self.screen = screen

    def display_map(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            for i in self._rooms:
                i_room_id = i.get_room_id()
                room_coordinate = (self._screen_dimensions / 2) + (i_room_id[0] * 50) - (i_room_id[1] * 100)
                pygame.draw.circle(self.screen, (255, 255, 255), [room_coordinate, i_room_id[0] * 250], 10)
                


class Room:
    def __init__(self, room_id, layout, combat_objects):
        self._room_id = room_id
        self._layout = layout
        self._combat_objects = combat_objects

    def get_room_id(self):
        return self._room_id