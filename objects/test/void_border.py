import pygame


class VoidBorder:
    def __init__(self, GAME):
        self.GAME = GAME
        self.SURFACE_SIZE = self.GAME.SURFACE_SIZE
        self.SURFACE = self.GAME.SURFACE

        self.player = self.GAME.player
        self.soldiers = self.GAME.soldier_group.soldiers

        self.border_y_pos = self.SURFACE_SIZE[1] - 20

    def update(self):
        if self.player.rect.bottom + self.player.velocity_y > self.border_y_pos:
            self.player.velocity_y = self.border_y_pos - self.player.rect.bottom

        for soldier in self.soldiers:
            if soldier.rect.bottom + soldier.velocity_y > self.border_y_pos:
                soldier.velocity_y = self.border_y_pos - soldier.rect.bottom

    def draw(self):
        pygame.draw.line(self.SURFACE, (0, 255, 0), (0, self.border_y_pos),
                         (self.SURFACE_SIZE[0], self.border_y_pos))
