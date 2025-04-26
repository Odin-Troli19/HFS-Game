import pygame
import os

class IntroAnimation:
    def __init__(self, window):
        self.window = window
        self.frames = []
        self.load_frames()
        self.frame_index = 0

    def load_frames(self):
        folder = "assets/animations/"
        for filename in sorted(os.listdir(folder)):
            if filename.endswith(".png"):
                frame = pygame.image.load(os.path.join(folder, filename)).convert_alpha()
                self.frames.append(frame)

    def play(self):
        clock = pygame.time.Clock()
        playing = True
        while playing:
            clock.tick(15)  # 15 FPS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.window.fill((0, 0, 0))

            if self.frame_index < len(self.frames):
                self.window.blit(self.frames[self.frame_index], (0, 0))
                self.frame_index += 1
            else:
                playing = False

            pygame.display.update()
