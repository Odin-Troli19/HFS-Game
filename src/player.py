import pygame
from settings import *

class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed = PLAYER_SPEED
        self.size = PLAYER_SIZE
        self.color = RED
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self, keys):
        if keys[pygame.K_LEFT]: self.x -= self.speed
        if keys[pygame.K_RIGHT]: self.x += self.speed
        if keys[pygame.K_UP]: self.y -= self.speed
        if keys[pygame.K_DOWN]: self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
