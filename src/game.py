import pygame
from player import Player
from area import Area
from stats import Stats
from ui import draw_stats
from settings import *

class Game:
    def __init__(self, window):
        self.window = window
        self.player = Player()
        self.stats = Stats()
        self.areas = [
            Area("Gym", pygame.Rect(100, 100, 150, 100)),
            Area("Library", pygame.Rect(550, 100, 150, 100)),
            Area("Dorm", pygame.Rect(100, 400, 150, 100)),
            Area("Field", pygame.Rect(550, 400, 150, 100))

        ]

    def update(self, keys):
        self.player.move(keys)
        for area in self.areas:
            if self.player.rect.colliderect(area.rect):
                self.stats.perform_activity(area.name)
                self.player.x, self.player.y = WIDTH // 2, HEIGHT // 2
                self.player.rect.topleft = (self.player.x, self.player.y)

        if self.stats.energy == 0:
            pygame.time.delay(1000)
            self.stats.new_day()

    def draw(self):
        self.window.fill(WHITE)
        for area in self.areas:
            area.draw(self.window)
        self.player.draw(self.window)
        draw_stats(self.window, self.stats)
        pygame.display.update()
