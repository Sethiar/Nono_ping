import pygame
from menu import MenuScreen

pygame.init()

fenetre = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Nono Pong")

menu_screen = MenuScreen(fenetre)

if __name__ == "__main__":
    menu_screen.run_menu()