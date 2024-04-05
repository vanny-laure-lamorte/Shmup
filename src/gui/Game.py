import pygame
from src.pygame_manager.Element import Element
from src.entities.Dragon import Dragon

class Game(Element, Dragon):
    def __init__(self): 
        Element.__init__(self)
        Dragon.__init__(self)
        self.running = True

        self.b1 = pygame.image.load(f"assets/image/game/balloon1.png").convert_alpha()
        self.b2 = pygame.image.load(f"assets/image/game/balloon2.png").convert_alpha()
        self.b3 = pygame.image.load(f"assets/image/game/balloon3.png").convert_alpha()
        self.b4 = pygame.image.load(f"assets/image/game/balloon4.png").convert_alpha()
        self.balloon = [self.b1, self.b2, self.b3, self.b4]

        self.img_back = pygame.image.load(f"assets/image/game/background.png").convert_alpha()
        self.img_castle = pygame.image.load(f"assets/image/game/game_castle.png").convert_alpha()

        self.rect_option = pygame.image.load(f"assets/image/game/game_rect.png").convert_alpha()

    def background(self):

        # Bacckground
        self.img_background(self.W // 2, self.H // 2, self.W, self.H, self.img_back)

        # Tour
        self.img_not_center("Castle", -90, 20, 450, 615, self.img_castle)

        # Rect
        self.img_not_center("Rect", 50, 20, 100, 50, self.rect_option)



    def dragon_visual(self):
        if self.moving_left:
            self.img_mir("Dragon_red", self.dragon_x,  self.dragon_y, 200,200,self.red_frames[self.dragon_frame])
        else:
            self.img_center("Dragon_red", self.dragon_x, self.dragon_y, 200,200,self.red_frames[self.dragon_frame])
        # self.img_center("Dragon_blue", 700,350,200,200,self.blue_frames[self.dragon_frame])
        self.dragon_frame += 1 
        self.dragon_frame %= len(self.red_frames)

    def balloon_visual(self):
        if self.dragon_frame < 6:
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
            self.start_ball = self.ball_x
        else:
            self.img_center("Dragon_red", self.ball_x, self.ball_y, 70, 70,self.fireball[self.fireball_frame])
            self.fireball_frame += 1 
            self.fireball_frame %= len(self.fireball)

            if self.ball_x < self.start_ball + 500:
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

            self.background()
            self.dragon_movement()
            self.dragon_visual()
            self.balloon_visual()
            self.fireball_visual((self.dragon_x, self.dragon_y))
            self.update()
