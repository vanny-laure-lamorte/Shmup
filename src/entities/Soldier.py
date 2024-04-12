import pygame, os, random

class Soldier:
    def __init__(self):
        self.soldier_frames_walk = [pygame.image.load(os.path.join(f"assets/image/game/soldier/soldier_walk_{i:02}.png")).convert_alpha() for i in range(1, 9)]
        self.soldier_frames_run = [pygame.image.load(os.path.join(f"assets/image/game/soldier/soldier_run_{i:02}.png")).convert_alpha() for i in range(1, 8)]
        self.soldier_frames_dead = [pygame.image.load(os.path.join(f"assets/image/game/soldier/soldier_dead_{i:02}.png")).convert_alpha() for i in range(1, 7)]
        self.soldier_frames = {}
        self.soldier = [self.soldier_frames_walk, self.soldier_frames_run]

        self.soldier_frame = 0
        self.soldier_speed = 0.52
        self.soldier_frame_speed = 0.14
        self.soldier_list = []
        self.soldier_health = [150, 125, 100, 75]

        self.soldier_type_value = [
            (0,0,0),
            (0 ,0 ,0.1),  # Level 1
            (0, 0, 0.3),   # Level 2
            (0.05, 0.2, 0.5),  # Level 3
            (0.1, 0.3, 0.5),   # Level 4
            (0.15, 0.3, 0.5),  # Level 5
            (0.2, 0.3, 0.5),   # Level 6
            (0.25, 0.3, 0.5),  # Level 7
            (0.3, 0.3, 0.5),   # Level 8
            (0.35, 0.3, 0.5),  # Level 9
            (0.4, 0.3, 0.3)    # Level 10
        ]

        # self.balloon_creation(1) #Test de la méthode

    def soldier_creation(self, level):
        nb_soldier = random.randint(level, level + 1)
        if level > 9:
            level = 9
        for i in range(nb_soldier):
            rand_val = random.random()

            if rand_val <= self.soldier_type_value[level][0]:
                soldier_type = 0
            elif rand_val <= self.soldier_type_value[level][1]:
                soldier_type = 1
            elif rand_val <= self.soldier_type_value[level][2]:
                soldier_type = 2
            else:
                soldier_type = 3

            pos_x_soldier = random.randint(1350, 1500)
            pos_y_soldier = 590
            self.soldier_list.append((pos_x_soldier, pos_y_soldier, self.soldier_health[soldier_type], soldier_type, False))