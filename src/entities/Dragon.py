import pygame

class Dragon:
    def __init__(self):
        # Dragon sprites
        self.d1 = pygame.image.load(f"assets/image/game/dragon1.png").convert_alpha()
        self.d2 = pygame.image.load(f"assets/image/game/dragon2.png").convert_alpha()
        self.d3 = pygame.image.load(f"assets/image/game/dragon3.png").convert_alpha()
        self.d4 = pygame.image.load(f"assets/image/game/dragon4.png").convert_alpha()
        self.d5 = pygame.image.load(f"assets/image/game/dragon5.png").convert_alpha()
        self.d6 = pygame.image.load(f"assets/image/game/dragon6.png").convert_alpha()
        self.blue_frames = [self.d1 ,self.d1 ,self.d1 ,self.d1 ,self.d2 ,self.d2 ,self.d2 ,self.d2 ,self.d3 ,self.d3 ,self.d3 ,self.d3] 
        self.red_frames = [self.d4 ,self.d4 ,self.d4 ,self.d4 ,self.d5 ,self.d5 ,self.d5 ,self.d5 ,self.d6 ,self.d6 ,self.d6 ,self.d6]
        self.dragon_frame = 0

        # Fireball sprites

        self.fb1 = pygame.image.load(f"assets/image/game/fireball/fireball1.png").convert_alpha()
        self.fb2 = pygame.image.load(f"assets/image/game/fireball/fireball2.png").convert_alpha()
        self.fb3 = pygame.image.load(f"assets/image/game/fireball/fireball3.png").convert_alpha()
        self.fb4 = pygame.image.load(f"assets/image/game/fireball/fireball4.png").convert_alpha()
        self.fb5 = pygame.image.load(f"assets/image/game/fireball/fireball5.png").convert_alpha()
        self.fb6 = pygame.image.load(f"assets/image/game/fireball/fireball6.png").convert_alpha()
        self.fb7 = pygame.image.load(f"assets/image/game/fireball/fireball7.png").convert_alpha()
        self.fb8 = pygame.image.load(f"assets/image/game/fireball/fireball8.png").convert_alpha()
        self.fb9 = pygame.image.load(f"assets/image/game/fireball/fireball9.png").convert_alpha()
        self.fb10 = pygame.image.load(f"assets/image/game/fireball/fireball10.png").convert_alpha()
        self.fireball = [self.fb1, self.fb2, self.fb3, self.fb4, self.fb5, self.fb6, self.fb7, self.fb8, self.fb9, self.fb10]
        self.fireball_frame = 0
        
        self.move_x, self.move_y = 0, 0
        self.moving_down, self.moving_left, self.moving_right, self.moving_up = False, False, False, False

        self.ball_moving = False
        self.ball_x, self.ball_y = 0, 0
        self.start_ball = 0

    def dragon_movement(self):
        self.dragon_x = self.move_x + 300
        self.dragon_y = self.move_y + 360

        if self.moving_left:
            if self.dragon_x > 100:
                self.move_x -= 30
        elif self.moving_right:
            if self.dragon_x < 1150:
                self.move_x += 30
        elif self.moving_up:
            if self.dragon_y > 100:
                self.move_y -= 30
        elif self.moving_down:
            if self.dragon_y < 600:
                self.move_y += 30
        