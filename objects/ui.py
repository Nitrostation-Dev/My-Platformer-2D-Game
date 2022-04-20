import pygame
from utils.surface_rect import *


class UI:
    def __init__(self, GAME):
        self.GAME = GAME
        self.WINDOW_SIZE = self.GAME.WINDOW_SIZE
        self.SCREEN = self.GAME.SCREEN
        self.GAME_CLOCK = self.GAME.CLOCK

    def event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        # FPS
        fps_surface, fps_rect = get_surface_rect_text(
            './assets/fonts/bungee.ttf', 16, str(f'FPS: {int(self.GAME_CLOCK.get_fps())}'), (255, 255, 255), True)
        fps_rect.bottomleft = (0, self.WINDOW_SIZE[1])

        # Drawing
        self.SCREEN.blit(fps_surface, fps_rect)
