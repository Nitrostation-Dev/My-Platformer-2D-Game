import pygame


class Bullet:
    def __init__(self, BULLET_GROUP, GAME, POS, DIRECTION, ID):
        self.BULLET_GROUP = BULLET_GROUP
        self.GAME = GAME
        self.SURFACE = self.GAME.SURFACE
        self.SURFACE_SIZE = self.GAME.SURFACE_SIZE
        self.BULLET_SPEED = self.GAME.BULLET_SPEED
        self.DIRECTION = DIRECTION
        self.ID = ID

        # Surface and Rect
        self.image = pygame.Surface((5, 3))
        self.rect = self.image.get_rect()
        if self.DIRECTION == 1:
            self.rect.midleft = POS
        else:
            self.rect.midright = POS

        self.image.fill((255, 0, 0))
        
        # Player
        self.player = self.GAME.player
        
        # Enemy
        self.enemies = self.GAME.enemies.enemies

    def kill_self(self):
        del self
        
    def kill(self):
        self.BULLET_GROUP.kill_bullet(self.ID)

    def collisions(self):
        if self.DIRECTION == 1 and self.rect.left >= self.SURFACE_SIZE[0] or self.DIRECTION == -1 and self.rect.right <= 0:
            self.kill()
            
        # Checking Collision with player:
        if self.rect.colliderect(self.player) and self.player.alive:
            self.player.kill()
            self.kill()
        
        for enemy in self.enemies:
            if self.rect.colliderect(enemy.rect) and enemy.alive:
                enemy.kill()
                enemy.image.fill((255, 255, 255))
                self.kill()
                
    def move(self):
        self.rect.x += self.DIRECTION * self.BULLET_SPEED

    def update(self):
        self.move()
        self.collisions()

    def draw(self):
        self.SURFACE.blit(self.image, self.rect)


class BulletGroup:
    def __init__(self, GAME):
        self.GAME = GAME

        self.bullet_id = 0
        self.bullets = []

    def add_bullet(self, POS, DIRECTION):
        self.bullets.append(
            Bullet(self, self.GAME, POS, DIRECTION, self.bullet_id))
        self.bullet_id += 1

    def kill_bullet(self, bullet_id):
        for i, bullet in enumerate(self.bullets):
            if bullet.ID == bullet_id:
                self.bullets.pop(i)
                bullet.kill()

    def update(self):
        for bullet in self.bullets:
            bullet.update()

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
