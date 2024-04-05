import pygame, os, random

class Balloon:
    def __init__(self):
        self.balloon = [pygame.image.load(os.path.join(f"assets/image/game/balloon{i}.png")).convert_alpha() for i in range(1, 5)]

        self.explosion = [pygame.image.load(os.path.join(f"assets/image/game/explosion/explosion{i}.png")).convert_alpha() for i in range(1, 8)]
        self.explosion = [frame for frame in self.explosion for _ in range(3)]
        self.explosion_frames = {}

        self.balloon_list = []
        self.balloon_health = [400, 300, 200, 100]

        self.balloon_type_value = [
            (0 ,0 ,0.1),  # Level 1
            (0, 0, 0.3),   # Level 2
            (0.05, 0.2, 0.5),  # Level 3
            (0.1, 0.3, 0.5),   # Level 4
            (0.15, 0.3, 0.5),  # Level 5
            (0.2, 0.3, 0.5),   # Level 6
            (0.25, 0.3, 0.5),  # Level 7
            (0.3, 0.3, 0.5),   # Level 8
            (0.35, 0.3, 0.5),  # Level 9
            (0.4, 0.3, 0.5)    # Level 10
        ]

        self.balloon_creation(0) #Test de la méthode

    def balloon_creation(self, level):
        nb_balloons = random.randint(level + 2, level + 3)

        for i in range(nb_balloons):
            rand_val = random.random()

            if rand_val <= self.balloon_type_value[level][0]:
                balloon_type = 0
            elif rand_val <= self.balloon_type_value[level][1]:
                balloon_type = 1
            elif rand_val <= self.balloon_type_value[level][2]: 
                balloon_type = 2
            else:
                balloon_type = 3

            pos_x_balloon = random.randint(1350, 1500)
            pos_y_balloon = random.randint(55, 300)
            self.balloon_list.append((pos_x_balloon, pos_y_balloon, self.balloon_health[balloon_type], balloon_type, False))



