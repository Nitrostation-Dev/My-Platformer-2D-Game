import pygame


class Explosion:
    def __init__(self, GAME, EXPLOSION_GROUP, POS, DAMAGE, EXPLOSION_RADIUS, ID):
        # Game
        self.GAME = GAME
        self.SURFACE = self.GAME.SURFACE
        self.EXPLOSION_GROUP = EXPLOSION_GROUP
        self.EXPLOSION_RADIUS = EXPLOSION_RADIUS
        self.DAMAGE = DAMAGE
        self.ID = ID

        # TODO: Make explosion more realistic by making it spawning big then slowly becomming small

        # Image
        self.image = pygame.Surface(self.EXPLOSION_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.midright = POS

        # Mechanics
        self.explode = True
        self.explosion_timer = pygame.time.get_ticks()
        self.explosion_cooldown = 1000

        self.image.fill((255, 75, 0))

    def kill(self):
        self.EXPLOSION_GROUP.kill_explosion(self.ID)

    def kill_self(self):
        del self

    def collisions(self):
        pass # TODO: Make it so explosion damages entities

    def update(self):
        if self.explode:
            self.collisions()
            if pygame.time.get_ticks() - self.explosion_timer >= self.explosion_cooldown:
                self.kill()
                # self.explode = False

    def draw(self):
        if self.explode:
            self.SURFACE.blit(self.image, self.rect)


class ExplosionGroup:
    def __init__(self, GAME):
        # Game
        self.GAME = GAME

        self.explosion_id = 0
        self.explosions = []

    def kill_explosion(self, explosion_id):
        for i, explosion in enumerate(self.explosions):
            if explosion.ID == explosion_id:
                self.explosions.pop(i)
                explosion.kill_self()

    def create_explosion(self, POS, DAMAGE, EXPLOSION_RADIUS):
        self.explosions.append(
            Explosion(self.GAME, self, POS, DAMAGE, EXPLOSION_RADIUS, self.explosion_id))
        self.explosion_id += 1

    def update(self):
        for explosion in self.explosions:
            explosion.update()

    def draw(self):
        for explosion in self.explosions:
            explosion.draw()
