import pygame
from settings import *

class Button:
    def __init__(self, text, x, y, width, height, font, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color_idle = GRAY
        self.color_hover = BLUE
        self.font = font
        self.action = action

    def draw(self, window):
        mouse_pos = pygame.mouse.get_pos()
        color = self.color_hover if self.rect.collidepoint(mouse_pos) else self.color_idle
        pygame.draw.rect(window, color, self.rect)
        text_surf = self.font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        window.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if self.action:
                self.action()

class MainMenu:
    def __init__(self, window):
        self.window = window
        self.buttons = []
        self.running = True
        self.font_big = pygame.font.SysFont("Arial", 50)
        self.font_small = pygame.font.SysFont("Arial", 30)

        self.settings_icon = pygame.image.load("assets/ui/settings_icon.png").convert_alpha()
        self.share_icon = pygame.image.load("assets/ui/share_icon.png").convert_alpha()

        self.create_buttons()

    def create_buttons(self):
        center_x = WIDTH // 2 - 100
        self.buttons.append(Button("New Game", center_x, 200, 200, 50, self.font_small, self.new_game))
        self.buttons.append(Button("Continue Game", center_x, 270, 200, 50, self.font_small, self.continue_game))
        self.buttons.append(Button("Tutorial", center_x, 340, 200, 50, self.font_small, self.tutorial))

    def new_game(self):
        print("Starting new game...")
        self.running = False  # later connect to your game engine

    def continue_game(self):
        print("Loading saved game...")

    def tutorial(self):
        print("Showing tutorial...")

    def draw(self):
        self.window.fill(WHITE)

        # Title
        title_surf = self.font_big.render("High School Football Star", True, BLACK)
        title_rect = title_surf.get_rect(center=(WIDTH // 2, 100))
        self.window.blit(title_surf, title_rect)

        # Buttons
        for button in self.buttons:
            button.draw(self.window)

        # Settings button
        self.window.blit(self.settings_icon, (WIDTH - 80, 20))
        # Share button
        self.window.blit(self.share_icon, (WIDTH - 80, 100))

        pygame.display.update()

    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                for button in self.buttons:
                    button.is_clicked(event)

            self.draw()
