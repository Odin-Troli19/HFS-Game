import pygame
from settings import *

def draw_stats(window, stats):
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f"Day: {stats.day} | STR: {stats.strength} | INT: {stats.intelligence} | STA: {stats.stamina} | ENG: {stats.energy}", True, BLACK)
    window.blit(text, (20, 20))
