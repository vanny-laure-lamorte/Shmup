import os, pygame
class Dragon:
    def __init__(self):
        self.red_frames = [pygame.image.load(os.path.join(f"assets/image/game/dragon3/dragon{i}.png")).convert_alpha() for i in range(13, 25)]
        self.black_frames = [pygame.image.load(os.path.join(f"assets/image/game/dragon3/dragon{i}.png")).convert_alpha() for i in range(1, 13)]

        self.fireball = [pygame.image.load(os.path.join(f"assets/image/game/fireball/fireball{i}.png")).convert_alpha() for i in range(1, 11)]

        self.dragon_frame = 0
        self.fireball_frame = 0
        self.dragon_attackspeed = 0.15
        self.dragon_attack_frame = 0
        self.dragon_attack = False

        self.dragon_x, self.dragon_y = 345, 285
        self.dragon_damage = 30
        self.bonus_range_fireball = 300

        self.fireballs_list = []

        self.move_x, self.move_y = 0, 0
        self.moving_down, self.moving_left, self.moving_right, self.moving_up = False, False, False, False
        self.ball_x, self.ball_y = 0, 0

    def dragon_movement(self):
        self.dragon_x = self.move_x +345
        self.dragon_y = self.move_y +285
        if self.moving_left:
            if self.dragon_x > 75:
                self.move_x -= 7.5
        elif self.moving_right:
            if self.dragon_x < 1175:
                self.move_x += 7.5
        elif self.moving_up:
            if self.dragon_y > 75:
                self.move_y -= 7.5
        elif self.moving_down:
            if self.dragon_y < 330:
                self.move_y += 7.5
