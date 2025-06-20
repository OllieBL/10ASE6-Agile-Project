import pygame
from pygame.locals import *
from sys import exit
import random
import math
import combat_objects
import board

# The map that the player moves around on to complete the game
class Map:
    def __init__(self, room_quantity, screen_dimensions, screen, player):
        self._room_quantity = room_quantity
        self._rooms = []
        self._screen_dimensions = screen_dimensions
        self.screen = screen
        self.player = player
        self._text = pygame.font.SysFont('calibri.ttf', 30)
        self._player_dead = False
        
        self.createMap()

    # creates the map and the rooms inside of it, also randomising the type of room it is
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


            self._rooms.append(Room([row, column], room_type, self.player, self.screen))

        self._rooms.append(Room([row+2, (row+1)/2], 0, self.player, self.screen))
        self._room_pos_list = [i.get_room_id() for i in self._rooms]

    # displays the map and also allows the player to interact with it
    def display_map(self):
        self.screen.fill((0, 0, 0))

        
            
        left_button_text = self._text.render('Go left', False, (0, 0, 0))
        right_button_text = self._text.render('Go right', False, (0, 0, 0))

        left_button_text_rect = left_button_text.get_rect()
        right_button_text_rect = right_button_text.get_rect()

        left_button_text_rect.center = (200, 325)
        right_button_text_rect.center = (350, 325)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_buttons()

            if self._player_dead == True:
                break

            for i in self._rooms:
                i_room_id = i.get_room_id()
                coord_calculator = lambda a, b, c : (a / 2) - (b * 50) + (c * 100) # nicer than just copying to everywhere that it's used

                room_coordinate = coord_calculator(self._screen_dimensions[0], i_room_id[0], i_room_id[1])

                # generates the circles on the screen, with different colours for different room types, also draws lines between them
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

            self.screen.blit(left_button_text, left_button_text_rect)
            self.screen.blit(right_button_text, right_button_text_rect)

            pygame.display.flip()

    def check_buttons(self):
        mouse_pos = pygame.mouse.get_pos()

        if 300 <= mouse_pos[0] <= 400 and 300 <= mouse_pos[1] <= 350:
            old_player_pos = self.player.get_pos()
            self.player.set_pos([old_player_pos[0] + 1, old_player_pos[1] + 1])
            test = self._rooms[self._room_pos_list.index(self.player.get_pos())].generate_layout()
            if test != False:
                self._player_dead = (self._rooms[self._room_pos_list.index(self.player.get_pos())].get_layout()).display_board()
                self.player.get_combat_state().set_damage(self.player.get_combat_state().get_damage() + 1)
            else:
                print('you got stuff')
                results = self._rooms[self._room_pos_list.index(self.player.get_pos())].get_layout()
                if results[1] == 0:
                    self.player.get_combat_state().change_health(results[0])
            
            self.screen.fill((0, 0, 0))

        if 150 <= mouse_pos[0] <= 250 and 300 <= mouse_pos[1] <= 350:
            old_player_pos = self.player.get_pos()
            self.player.set_pos([old_player_pos[0] + 1, old_player_pos[1]])
            test = self._rooms[self._room_pos_list.index(self.player.get_pos())].generate_layout()
            if test != False:
                self._player_dead = (self._rooms[self._room_pos_list.index(self.player.get_pos())].get_layout()).display_board()
                self.player.get_combat_state().set_damage(self.player.get_combat_state().get_damage() + 1)
            else:
                print('you got stuff')
                results = self._rooms[self._room_pos_list.index(self.player.get_pos())].get_layout()
                if results[1] == 0:
                    self.player.get_combat_state().change_health(results[0])
            
            self.screen.fill((0, 0, 0))
        

                


class Room:
    def __init__(self, room_id, room_type, player, screen):
        self._room_id = room_id
        self._layout = []
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
            test_layout = random.randrange(0,1)
            if test_layout == 0:
                multiplier = 2
            else:
                multiplier = 1
            self._layout = [self._room_id[0] * multiplier, test_layout]
            return False
        if self._room_type == 1:
            enemy_pos_list = []
            number_of_enemies = self._room_id[0] * 3
            for i in range(number_of_enemies):
                while True:
                    random_pos = [random.randrange(0, 20), random.randrange(0, 16)]
                    if random_pos not in enemy_pos_list:
                        combat_objects_list.append(combat_objects.Enemy(10, 1, 'enemy', random_pos, 'Images and other files/enemy_art.png'))
                        break
        else:
            enemy_pos_list = []
            number_of_enemies = self._room_id[0] * 2
            for i in range(number_of_enemies):
                while True:
                    random_pos = [random.randrange(0, 20), random.randrange(0, 16)]
                    if random_pos not in enemy_pos_list:
                        combat_objects_list.append(combat_objects.Enemy(10, 1, 'enemy', random_pos, 'Images and other files/enemy_art.png'))
                        break
        self._layout = board.CombatBoard(combat_objects_list, [20, 20], self.screen)