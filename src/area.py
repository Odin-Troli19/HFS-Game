import pygame
from settings import *

class Area:
    def __init__(self, name, rect):
        self.name = name
        self.rect = rect
        self.color = GREEN

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        font = pygame.font.SysFont(\"Arial\", 18)
        label = font.render(self.name, True, BLACK)
        window.blit(label, (self.rect.x + 10, self.rect.y + 10))
