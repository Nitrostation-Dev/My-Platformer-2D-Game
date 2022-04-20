import pygame


class Rocket:
    def __init__(self, GAME, ROCKET_GROUP, POS, DIRECTION):
        self.GAME = GAME
        self.ROCKET_GROUP = ROCKET_GROUP
        self.SURFACE = self.GAME.SURFACE
        self.SURFACE_SIZE = self.GAME.SURFACE_SIZE
        self.DIRECTION = DIRECTION
        self.ROCKET_SPEED = self.GAME.ROCKET_SPEED
        self.explosion_group = self.GAME.explosion_group
        self.EXPLOSION_RADIUS = self.GAME.ROCKET_EXPLOSION_RADIUS
        self.EXPLOSION_RADIUS = (self.EXPLOSION_RADIUS, self.EXPLOSION_RADIUS)

        # Image
        self.image = pygame.Surface((8, 3))
        self.rect = self.image.get_rect()
        if self.DIRECTION == 1:
            self.rect.midleft = POS
        else:
            self.rect.midright = POS

        self.image.fill((0, 0, 255))

    def kill_self(self):
        del self

    def kill(self):
        self.summon_explosion()
        self.ROCKET_GROUP.kill_rocket()
        self.GAME.player.can_fire_launcher = True
        self.kill_self()
        
        # TODO: Clean the whole code with health system

    def summon_explosion(self):
        if self.DIRECTION == 1:
            self.explosion_group.create_explosion(
                self.rect.midright, 25, self.EXPLOSION_RADIUS)
        else:
            self.explosion_group.create_explosion(
                (self.rect.left + self.EXPLOSION_RADIUS[0], self.rect.midleft[1]), 25, self.EXPLOSION_RADIUS)

    def collisions(self):
        if self.DIRECTION == 1 and self.rect.left >= self.SURFACE_SIZE[0] or self.DIRECTION == -1 and self.rect.right <= 0:
            self.kill()
            
        # TODO: Make the rocket collide with entities

    def update(self):
        self.rect.x += self.DIRECTION * self.ROCKET_SPEED
        self.collisions()

    def draw(self):
        self.SURFACE.blit(self.image, self.rect)


class RocketGroup:
    def __init__(self, GAME):
        self.GAME = GAME
        # TODO: Make the rocket firing system more better since only one rocket can be fired at a time
        self.rockets = []

    def add_rocket(self, POS, DIRECTION):
        self.rockets.append(Rocket(self.GAME, self, POS, DIRECTION))

    def kill_rocket(self):
        self.rockets = []

    def update(self):
        for rocket in self.rockets:
            rocket.update()

    def draw(self):
        for rocket in self.rockets:
            rocket.draw()
