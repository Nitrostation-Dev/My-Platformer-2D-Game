import pygame
from objects.interactables.knife import Knife


class Player:
    def __init__(self, GAME, POS):
        # Game
        self.GAME = GAME
        self.SURFACE = self.GAME.SURFACE
        self.GRAVITY = self.GAME.GRAVITY
        self.MAX_VEL_Y = self.GAME.MAX_VELOCITY_Y
        self.health = self.GAME.PLAYER_HEALTH

        # Rect
        self.image = pygame.Surface((16, 32))
        self.rect = self.image.get_rect()
        self.rect.center = POS

        # Movement Variables
        self.gravity = True
        self.can_interact = True
        self.moving_right = False
        self.moving_left = False
        self.direction = 1
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = self.GAME.player_speed
        self.jump_force = self.GAME.player_jump_force
        self.jumping = False
        self.can_jump = True
        self.dashing = False
        self.dash_distance = 35
        self.dash_distance_left = 0
        self.dash_speed = self.GAME.player_dash_speed
        self.can_dash = True
        self.countdown_dash = False
        self.dash_timer = 0
        self.dash_cooldown = 500

        # Variables
        self.alive = True
        self.can_swing_knife = True

        # Handling Surface
        self.image.fill((255, 0, 0))

        # Objects
        self.knife = Knife(self.GAME, self)

        # TODO: Fix No cooldown bullet and rocket firing

    def kill(self):
        self.alive = False

    def swing_knife(self):
        pos = ()
        if self.direction == 1:
            pos = self.rect.midright
        else:
            pos = self.rect.midleft
            
        self.knife.swing(pos, self.direction)
        self.can_swing_knife = False

    def move(self):
        if not self.alive:
            return

        if self.dashing:
            init_pos_x = self.rect.x

            self.rect.x += self.direction * self.dash_speed
            final_pos_x = self.rect.x

            self.dash_distance_left += final_pos_x - init_pos_x

            if self.direction == 1 and self.dash_distance_left >= self.dash_distance or self.direction == -1 and self.dash_distance_left <= -self.dash_distance:
                self.dash_finished()

        elif self.can_interact:
            # Moving Left and Right
            if self.moving_left:
                self.rect.x -= self.speed
                self.direction = -1
            if self.moving_right:
                self.rect.x += self.speed
                self.direction = 1

            # Jump
            # TODO: Fix multi jump while in air
            if self.jumping and self.can_jump:
                self.velocity_y = 0
                self.velocity_y -= self.jump_force
                self.jumping = False

        if self.gravity:
            # Gravity
            self.velocity_y += self.GRAVITY
            if self.velocity_y > self.MAX_VEL_Y:
                self.velocity_y = self.MAX_VEL_Y

        # Moving Rect
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

    def dash(self):
        if not self.can_dash:
            return

        self.dashing = True
        self.can_dash = False
        self.gravity = False
        self.can_interact = False
        self.velocity_y = 0
        self.dash_timer = pygame.time.get_ticks()
        self.dash_distance_left = 0
        
        # BRUH STUFF
        self.image.fill((175, 0, 0))

    def dash_finished(self):
        self.dashing = False
        self.gravity = True
        self.can_interact = True
        self.countdown_dash = True
        
        # BRUH STUFF
        self.image.fill((255, 0, 0))

    def handle_cooldowns(self):
        # Cooldown for dash rechanging
        if self.countdown_dash and pygame.time.get_ticks() - self.dash_cooldown >= self.dash_timer:
            self.countdown_dash = False
            self.can_dash = True

    def event(self, event):
        if not self.alive:
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.moving_left = True

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.moving_right = True

            if event.key == pygame.K_w or event.key == pygame.K_UP:
                self.jumping = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.moving_left = False

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.moving_right = False

        # Mouse Input
        if pygame.mouse.get_pressed()[0]:
            self.swing_knife()

        if pygame.mouse.get_pressed()[2]:
            self.dash()

    def update(self):
        self.move()
        self.handle_cooldowns()
        
        # Updating Objects
        self.knife.update()
        
        # Health
        if self.health <= 0:
            self.alive = False
            self.image.fill((255, 255, 255))

    def draw(self):
        self.SURFACE.blit(self.image, self.rect)
        # Drawing Objects
        self.knife.draw()
