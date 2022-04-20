from objects.entities.player import Player


class Soldier(Player):
    def __init__(self, GAME, POS):
        super().__init__(GAME, POS)
        self.health = self.GAME.SOLDIER_HEALTH
        self.hit = False
        self.image.fill((255, 255, 0))


class SoldierGroup:
    def __init__(self, GAME, SOLDIER_POSITIONS):
        self.GAME = GAME

        # Creating Enemies
        self.soldiers = []
        for position in SOLDIER_POSITIONS:
            self.soldiers.append(Soldier(self.GAME, position))

    def update(self):
        for soldier in self.soldiers:
            soldier.update()

    def draw(self):
        for soldier in self.soldiers:
            soldier.draw()
