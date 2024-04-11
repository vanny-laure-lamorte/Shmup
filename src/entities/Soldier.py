import pygame, os

class Soldier:
    def __init__(self):
        self.soldier_frames_walk = [pygame.image.load(os.path.join(f"assets/image/game/soldier/soldier_walk_{i:02}.png")).convert_alpha() for i in range(1, 9)]
        self.soldier_frames_run = [pygame.image.load(os.path.join(f"assets/image/game/soldier/soldier_run_{i:02}.png")).convert_alpha() for i in range(1, 8)]
        self.soldier_frames_dead = [pygame.image.load(os.path.join(f"assets/image/game/soldier/soldier_dead_{i:02}.png")).convert_alpha() for i in range(1, 7)]

        self.soldier_frame = 0
        self.soldier_speed = 0.7
        self.soldier_frame_speed = 0.35
        self.soldier_x, self.soldier_y = 1200, 575
        self.is_dead = False

    def soldier_movement(self):
        if not self.is_dead:
            self.soldier_x -= self.soldier_speed
