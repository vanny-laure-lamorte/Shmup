import pygame
from src.pygame_manager.Element import Element
from src.entities.Dragon import Dragon
from src.entities.Balloon import Balloon

class Game(Element, Dragon, Balloon):
    def __init__(self): 
        Element.__init__(self)
        Dragon.__init__(self)
        Balloon.__init__(self)
        self.running = True
        self.explosion_list = []
        self.background = pygame.image.load(f"assets/image/game/background.png").convert_alpha()

    def dragon_visual(self):
        if self.moving_left:
            self.img_mirror("Dragon_red", self.dragon_x,  self.dragon_y, 177,162,self.red_frames[self.dragon_frame])
        else:
            self.img_center("Dragon_red", self.dragon_x, self.dragon_y, 177,162,self.red_frames[self.dragon_frame])
        # self.img_center("Dragon_blue", 700,350,200,200,self.blue_frames[self.dragon_frame]) 
        self.dragon_frame += 1
        self.dragon_frame %= len(self.red_frames)

    def balloon_visual(self):
        for i, (x, y, health) in enumerate(self.balloon_list):
            color = self.green if health * 100 // self.balloon_health > 30 else self.red
            self.img_center("Balloon", x , y, 40, 64, self.balloon[0])
            # Vie des ballons
            if health < self.balloon_health:
                self.rect_full_not_centered(color, x +30 , y - 32, health * 60 // self.balloon_health, 6, 0)
                self.rect_border(self.black, x, y - 35, 60, 6, 1, 0)
            if x > 750:
                self.balloon_list[i] = (x - 1, y, health)

    def fireball_visual(self):
        for i, (ball_x, ball_y, ball_x_orig, ball_moving) in enumerate(self.fireballs_list):
            if ball_moving:
                self.img_center("Dragon_red", ball_x, ball_y, 70, 70, self.fireball[self.fireball_frame])
                self.fireball_frame += 1
                self.fireball_frame %= len(self.fireball)

                ball_x += 15 

                self.fireballs_list[i] = (ball_x, ball_y, ball_x_orig, ball_moving)

                if ball_x > ball_x_orig + 500: 
                    self.fireballs_list[i] = (ball_x_orig, ball_y, ball_x_orig, False)
                    del self.fireballs_list[i]

    def explosion_visual(self):
        for i, (explo_x, explo_y) in enumerate(self.explosion_list):
                if (explo_x, explo_y) not in self.explosion_frames:
                    self.explosion_frames[(explo_x, explo_y)] = 0
                if self.explosion_frames[(explo_x, explo_y)] < len(self.explosion) - 1:
                    self.img_center("explosion", explo_x, explo_y, 60, 88, self.explosion[self.explosion_frames[(explo_x, explo_y)]])
                    self.explosion_frames[(explo_x, explo_y)] += 1
                else:
                    del self.explosion_list[i]
                    del self.explosion_frames[(explo_x, explo_y)]

    def check_target(self):
        for i, (balloon_x, balloon_y, health) in enumerate(self.balloon_list):
            for j, (ball_x, ball_y, ball_x_orig, status) in enumerate(self.fireballs_list):
                if (balloon_x - 15 <= ball_x <= balloon_x + 15) and (balloon_y - 35 <= ball_y <= balloon_y + 35):
                    if health > self.dragon_damage:
                        self.balloon_list[i] = (balloon_x, balloon_y, health - self.dragon_damage)
                        del self.fireballs_list[j]
                    else:
                        self.explosion_list.append((balloon_x, balloon_y))
                        del self.balloon_list[i]
                        del self.fireballs_list[j]


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
                        self.fireballs_list.append((self.dragon_x, self.dragon_y, self.dragon_x, True))
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
            self.fireball_visual()
            self.check_target()
            self.explosion_visual()
            self.update()