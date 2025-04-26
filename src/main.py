import pygame
import sys
from animation import IntroAnimation
from menu import MainMenu
from settings import *

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("High School Football Star")

    # Optional: Background music
    # pygame.mixer.music.load("assets/sounds/menu_music.mp3")
    # pygame.mixer.music.play(-1)

    # Play intro animation
    intro = IntroAnimation(window)
    intro.play()

    # Show main menu
    menu = MainMenu(window)
    menu.run()

if __name__ == "__main__":
    main()
