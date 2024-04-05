import os, pygame
class Wizard:
    def __init__(self):
        self.wizard_frames = [pygame.image.load(os.path.join(f"assets/image/game/wizard/wizard{i}.png")).convert_alpha() for i in range(1, 11)]
        # self.thunderbolt = [pygame.image.load(os.path.join(f"assets/image/game/thunderbolt/thunderbolt{i}.png")).convert_alpha() for i in range(1, 4)]
        self.thunderbolt = pygame.image.load(os.path.join(f"assets/image/game/thunderbolt.png")).convert_alpha()
            
        self.wizard_frames = [frame for frame in self.wizard_frames for _ in range(2)]
        # self.thunderbolt = [frame for frame in self.thunderbolt for _ in range(3)]

        self.wiz_frame = 0
        # self.thunder_frame = 0

        self.wizard_attack = False
        self.dragon_damage = 10

        self.bolt_list = []
        self.move_wiz_x, self.move_wiz_y = 0, 0
        self.wizard_x, self.wizard_y = 285, 575
        self.moving_down, self.moving_left, self.moving_right, self.moving_up = False, False, False, False

        self.bolt_x, self.bolt_y = 0, 0

    def wizard_movement(self):
        self.wizard_x = self.move_wiz_x + 285
        self.wizard_y = self.move_wiz_y + 575
        if self.moving_left:
            if self.wizard_x > 75:
                self.move_wiz_x -= 15
        elif self.moving_right:
            if self.wizard_x < 1175:
                self.move_wiz_x += 15
        elif self.moving_up:
            if self.wizard_y > 450:
                self.move_wiz_y -= 15
        elif self.moving_down:
            if self.wizard_y < 590:
                self.move_wiz_y += 15

    def wizard_upgrade(self, bonus):

        self.wizard_frames = [pygame.image.load(os.path.join(f"assets/image/game/wizard/wizard{i}.png")).convert_alpha() for i in range(1, 11)]
        if bonus == 1:
            self.wizard_frames = [frame for frame in self.wizard_frames for _ in range(2)]
        elif bonus == 2:
            self.wizard_frames = [frame for frame in self.wizard_frames for _ in range(1)]
        elif bonus == 4:
            self.wizard_frames = self.wizard_frames[::2]
