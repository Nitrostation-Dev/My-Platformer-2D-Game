import pygame


def get_surface_rect_text(FONT_PATH, FONT_SIZE, MESSAGE, FONT_COLOR, ANTIALIAS):
    font = pygame.font.Font(FONT_PATH, FONT_SIZE)
    surface = font.render(MESSAGE, ANTIALIAS, FONT_COLOR)
    return surface, surface.get_rect()
