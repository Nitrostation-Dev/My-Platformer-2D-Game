import pygame


# TODO: Just make this class cleaner, clean this pls Very Impo
class Game:
    def __init__(self, SURFACE_SIZE, WINDOW_SIZE, WINDOW_FPS, WINDOW_CAPTION):
        self.SURFACE_SIZE = SURFACE_SIZE
        self.WINDOW_SIZE = WINDOW_SIZE
        self.WINDOW_FPS = WINDOW_FPS
        self.WINDOW_CAPTION = WINDOW_CAPTION

        # Opening Window
        pygame.init()
        self.SCREEN = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption(self.WINDOW_CAPTION)
        self.CLOCK = pygame.time.Clock()
        self.QUIT = False

        # Surface
        self.SURFACE = pygame.Surface(self.SURFACE_SIZE)

        # Game Variables
        self.GRAVITY = 0.45
        self.MAX_VELOCITY_Y = 15
        self.KNIFE_DAMAGE = 25
        
        # Health Variables
        self.PLAYER_HEALTH = 100
        self.SOLDIER_HEALTH = 75

        # UI
        from objects.ui import UI
        self.ui = UI(self)

        # Player
        from objects.entities.player import Player
        self.player_speed = 2
        self.player_dash_speed = self.player_speed * 8
        self.player_jump_force = 5
        self.player = Player(self, (100, 300))

        # Creating Soldier_group
        from objects.entities.soldier import SoldierGroup
        self.soldier_group = SoldierGroup(self, [(500, 300), (400, 300), (300, 300)])

        # Test Objects
        from objects.test.void_border import VoidBorder
        self.void_border = VoidBorder(self)

    def quit(self):
        self.QUIT = True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            # Handling Gameobject events
            self.player.event(event)
            self.ui.event(event)

    def update(self):
        # Updating GameObjects
        self.void_border.update()
        self.player.update()
        self.soldier_group.update()
        self.ui.update()

    def draw(self):
        self.SURFACE.fill((0, 0, 0))

        # Drawing GameObjects that draw on SURFACE
        self.player.draw()
        self.soldier_group.draw()
        self.void_border.draw()

        # Drawing Surface to Screen
        self.SCREEN.blit(pygame.transform.scale(
            self.SURFACE, self.WINDOW_SIZE), (0, 0))

        # Drawing Objects that draw on SCREEN
        self.ui.draw()

    def loop(self):
        while not self.QUIT:
            self.events()
            self.update()
            self.draw()

            pygame.display.update()
            self.CLOCK.tick(self.WINDOW_FPS)


if __name__ == '__main__':
    Game((640, 360), (1280, 720), 60, 'Platformer Shooter').loop()
