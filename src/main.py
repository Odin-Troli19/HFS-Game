import pygame
import sys
from game import Game
from settings import *

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("High School Football Star")
    clock = pygame.time.Clock()
    game = Game(window)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        game.update(keys)
        game.draw()

if __name__ == "__main__":
    main()
