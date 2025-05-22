import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((500, 500))
colour = (0, 0, 0)
width = int(screen.get_width())
height = int(screen.get_height())

while True:
    mx, my = pygame.mouse.get_pos()
    mouse_location = [mx, my]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == MOUSEBUTTONDOWN:
            if width/2-1 <= mouse_location[0] <= width/2+19 and height/2-1 <= mouse_location[1] <= height/2+39:
                colour = (255, 255, 255)
        
    

    screen.fill(colour)
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(((width/2)-1), ((height/2)-1), 20, 40))
    pygame.display.flip()