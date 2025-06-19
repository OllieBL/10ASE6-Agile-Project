import pygame
import menu


pygame.init()

screen = pygame.display.set_mode((1920, 1080))

menu0 = menu.Menu(screen)
menu0.display_menu()