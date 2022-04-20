import pygame


class Knife:
    def __init__(self, GAME, PLAYER):
        self.GAME = GAME
        self.DAMAGE = self.GAME.KNIFE_DAMAGE
        self.PLAYER = PLAYER
        self.SURFACE = self.GAME.SURFACE

        # Image
        self.image = pygame.Surface((16, 36))
        self.rect = self.image.get_rect()
        self.image.fill((175, 175, 175))

        # Variables
        self.direction = self.PLAYER.direction

        # Mechanics
        self.swinging = False
        self.swinging_timelimit_cooldown = 0
        self.swinging_timelimit_timer = 175
        self.recharge = False
        self.rechange_cooldown = 0
        self.rechange_timer = 200

    def update_position(self):
        # Updating Positions
        self.direction = self.PLAYER.direction
        if self.direction == 1:
            self.rect.centery = self.PLAYER.rect.centery
            self.rect.left = self.PLAYER.rect.right - (self.rect.width / 4)
        else:
            self.rect.centery = self.PLAYER.rect.centery
            self.rect.right = self.PLAYER.rect.left + (self.rect.width / 4)

    def handle_cooldowns(self):
        if self.swinging and pygame.time.get_ticks() - self.swinging_timelimit_cooldown >= self.swinging_timelimit_timer:
            self.swinging = False
            soldiers = self.GAME.soldier_group.soldiers
            for soldier in soldiers:
                soldier.hit = False
            
        if self.recharge and pygame.time.get_ticks() - self.rechange_cooldown >= self.rechange_timer:
            self.PLAYER.can_swing_knife = True

    def swing(self, POS, DIRECTION):
        if not self.swinging and not self.recharge:
            self.update_position()
            self.swinging = True
            self.swinging_timelimit_cooldown = pygame.time.get_ticks()

    def collisions(self):
        soldiers = self.GAME.soldier_group.soldiers
        for soldier in soldiers:
            if self.rect.colliderect(soldier.rect) and not soldier.hit:
                soldier.health -= self.DAMAGE
                soldier.hit = True

    def update(self):
        if self.swinging:
            self.update_position()
            self.collisions()
        self.handle_cooldowns()
        
    def draw(self):
        if self.swinging:
            self.SURFACE.blit(self.image, self.rect)
