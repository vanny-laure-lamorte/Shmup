import pygame, os, random

class Balloon:
    def __init__(self):
        self.balloon = [pygame.image.load(os.path.join(f"assets/image/game/balloon{i}.png")).convert_alpha() for i in range(1, 5)]

        self.explosion = [pygame.image.load(os.path.join(f"assets/image/game/explosion/explosion{i}.png")).convert_alpha() for i in range(1, 8)]
        self.explosion = [frame for frame in self.explosion for _ in range(3)]
        self.explosion_frames = {}

        self.balloon_list = []
        self.balloon_health = 100

        self.balloon_creation(4) #Test de la méthode

    def balloon_creation(self, level):
        nb_balloons = random.randint(level + 1, level + 2)

        for i in range(nb_balloons):
            pos_x_balloon = random.randint(1350, 1500)
            pos_y_balloon = random.randint(55, 300)
            self.balloon_list.append((pos_x_balloon, pos_y_balloon, self.balloon_health))
