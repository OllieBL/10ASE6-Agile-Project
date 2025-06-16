import pygame
from pygame.locals import *
from sys import exit
import map
import player
import combat_objects

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self._title_text = pygame.font.SysFont('calibri.ttf', 80)
        self._button_text = pygame.font.SysFont('calibri.ttf', 40)
    
    def display_menu(self):
        self.screen.fill((0, 0, 0))

        title = self._title_text.render('Wizard Game', False, (255, 255, 255))
        button_text = self._button_text.render('Start', False, (0, 0, 0))

        title_rect = title.get_rect()
        button_text_rect = button_text.get_rect()

        title_rect.center = (self.screen.get_width() // 2, 100)
        button_text_rect.center = (self.screen.get_width() // 2, 250)

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('hi')
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] >= 860 and mouse_pos[0] <= 1060 and mouse_pos[1] >= 200 and mouse_pos[1] <= 300:
                        player0 = player.Player([1, 0], combat_objects.Player(10, 2, 2, [], 'player', [0,0], 'Images and other files/test_image.png', []))
                        map0 = map.Map(21, [1920, 1080], screen, player0)
                        map0.display_map()

            self.screen.blit(title, title_rect)

            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                pygame.Rect(self.screen.get_width() // 2 - 100, 200, 200, 100)
            )

            self.screen.blit(button_text, button_text_rect)

            pygame.display.flip()



pygame.init()

screen = pygame.display.set_mode((1920, 1080))

menu = Menu(screen)
menu.display_menu()