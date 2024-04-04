import pygame
from src.pygame_manager.Element import Element

class Game(Element):
    def __init__(self): 
        Element.__init__(self)
        self.running = True
        self.d1 = pygame.image.load(f"assets/image/game/dragon1.png").convert_alpha()
        self.d2 = pygame.image.load(f"assets/image/game/dragon2.png").convert_alpha()
        self.d3 = pygame.image.load(f"assets/image/game/dragon3.png").convert_alpha()
        self.d4 = pygame.image.load(f"assets/image/game/dragon4.png").convert_alpha()
        self.d5 = pygame.image.load(f"assets/image/game/dragon5.png").convert_alpha()
        self.d6 = pygame.image.load(f"assets/image/game/dragon6.png").convert_alpha()
        self.blue_frames = [self.d1 ,self.d1 ,self.d1 ,self.d1 ,self.d2 ,self.d2 ,self.d2 ,self.d2 ,self.d3 ,self.d3 ,self.d3 ,self.d3] 
        self.red_frames = [self.d4 ,self.d4 ,self.d4 ,self.d4 ,self.d5 ,self.d5 ,self.d5 ,self.d5 ,self.d6 ,self.d6 ,self.d6 ,self.d6]

        self.b1 = pygame.image.load(f"assets/image/game/balloon1.png").convert_alpha()
        self.b2 = pygame.image.load(f"assets/image/game/balloon2.png").convert_alpha()
        self.b3 = pygame.image.load(f"assets/image/game/balloon3.png").convert_alpha()
        self.b4 = pygame.image.load(f"assets/image/game/balloon4.png").convert_alpha()
        self.balloon = [self.b1, self.b2, self.b3, self.b4]

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
        self.ball_moving = False
        self.ball_x, self.ball_y = 0, 0

        self.current_frame = 0
        self.fireball_frame = 0
        self.move_x, self.move_y = 0, 0
        self.moving_down, self.moving_left, self.moving_right, self.moving_up = False, False, False, False

        self.background = pygame.image.load(f"assets/image/game/background.png").convert_alpha()

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
        

    def dragon_visual(self):
        if self.moving_left:
            self.img_mir("Dragon_red", self.dragon_x,  self.dragon_y, 200,200,self.red_frames[self.current_frame])
        else:
            self.img_center("Dragon_red", self.dragon_x, self.dragon_y, 200,200,self.red_frames[self.current_frame])
        # self.img_center("Dragon_blue", 700,350,200,200,self.blue_frames[self.current_frame])
        self.current_frame += 1 
        self.current_frame %= len(self.red_frames)

    def balloon_visual(self):
        if self.current_frame < 6:
            self.img_center("Balloon", 1000,200,40,64, self.balloon[0])
            self.img_center("Balloon", 1100,150,40,64, self.balloon[1])
            self.img_center("Balloon", 900,300,40,64, self.balloon[2])
        else:
            self.img_center("Balloon", 1000,202,40,64, self.balloon[0])
            self.img_center("Balloon", 1100,152,40,64, self.balloon[1])
            self.img_center("Balloon", 900,302,40,64, self.balloon[2])

    def fireball_visual(self, position_ball):
        if not self.ball_moving:
            self.ball_x = position_ball[0] + 50
            self.ball_y = position_ball[1] + 10
        else:
            self.img_center("Dragon_red", self.ball_x, self.ball_y, 70, 70,self.fireball[self.fireball_frame])
            self.fireball_frame += 1 
            self.fireball_frame %= len(self.fireball)

            if self.ball_x < 800:
                self.ball_x += 20
            else:
                self.ball_moving = False

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.moving_down = True
                    elif event.key == pygame.K_UP:
                        self.moving_up = True
                    elif event.key == pygame.K_RIGHT:
                        self.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.moving_left = True
                    if event.key == pygame.K_SPACE:
                        self.ball_moving = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.moving_down = False
                    elif event.key == pygame.K_UP:
                        self.moving_up = False
                    elif event.key == pygame.K_RIGHT:
                        self.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.moving_left = False

            self.img_background(self.W // 2, self.H // 2, self.W, self.H, self.background)
            self.dragon_movement()
            self.dragon_visual()
            self.balloon_visual()
            self.fireball_visual((self.dragon_x, self.dragon_y))
            self.update()
