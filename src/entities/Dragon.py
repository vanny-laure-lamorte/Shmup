import os, pygame
class Dragon:
    def __init__(self):
        # self.red_frames = [pygame.image.load(os.path.join(f"assets/image/game/dragon2/dragon{i}.png")).convert_alpha() for i in range(1, 12)]
        # self.blue_frames = [pygame.image.load(os.path.join(f"assets/image/game/dragon{i}.png")).convert_alpha() for i in range(1, 4)]
        self.red_frames = [pygame.image.load(os.path.join(f"assets/image/game/dragon/dragon{i}.png")).convert_alpha() for i in range(4, 7)]
        self.fireball = [pygame.image.load(os.path.join(f"assets/image/game/fireball/fireball{i}.png")).convert_alpha() for i in range(1, 11)]

        # self.blue_frames = [frame for frame in self.blue_frames for _ in range(4)]
        self.red_frames = [frame for frame in self.red_frames for _ in range(3)]

        self.dragon_frame = 0
        self.fireball_frame = 0

        self.dragon_damage = 20

        self.fireballs_list = []

        self.move_x, self.move_y = 0, 0
        self.moving_down, self.moving_left, self.moving_right, self.moving_up = False, False, False, False

        self.ball_x, self.ball_y = 0, 0

    def dragon_movement(self):
        self.dragon_x = self.move_x + 300
        self.dragon_y = self.move_y + 360

        if self.moving_left:
            if self.dragon_x > 75:
                self.move_x -= 20
        elif self.moving_right:
            if self.dragon_x < 1175:
                self.move_x += 20
        elif self.moving_up:
            if self.dragon_y > 75:
                self.move_y -= 20
        elif self.moving_down:
            if self.dragon_y < 625:
                self.move_y += 20
