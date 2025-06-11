import pygame
import map
import player
import combat_objects


pygame.init()

screen = pygame.display.set_mode((1920, 1080))

player0 = player.Player(0, combat_objects.Player(10, 2, 2, [], 'player', [0,0], 'Images and other files/test_image.png', []))

map0 = map.Map(21, [1920, 1080], screen, player0)
map0.display_map()