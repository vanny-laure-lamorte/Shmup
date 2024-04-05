import pygame
from src.pygame_manager.Element import Element
from src.entities.Dragon import Dragon
from src.entities.Wizard import Wizard
from src.entities.Balloon import Balloon


class Game(Element, Dragon, Wizard, Balloon):
    def __init__(self): 
        Element.__init__(self)
        Dragon.__init__(self)
        Wizard.__init__(self)
        Balloon.__init__(self)
        self.running = True
        self.explosion_list = []
        self.background = pygame.image.load(f"assets/image/game/background1.png").convert_alpha()
        self.entity_moving = False

    def dragon_visual(self):

        if self.moving_left and self.entity_moving:
            self.img_mirror("Dragon_red", self.dragon_x,  self.dragon_y, 177,162,self.red_frames[self.dragon_frame])
        else:
            self.img_center("Dragon_red", self.dragon_x, self.dragon_y, 177,162,self.red_frames[self.dragon_frame])
        # self.img_center("Dragon_black", 700,350,200,200,self.black_frames[self.dragon_frame]) 
        self.dragon_frame += 1
        self.dragon_frame %= len(self.red_frames)

    def wizard_visual(self):

        if self.moving_left and not self.entity_moving:
            self.img_mirror("Wizard", self.wizard_x,  self.wizard_y, 140,130,self.wizard_frames[self.wiz_frame])
        else:
            self.img_center("Wizard", self.wizard_x,  self.wizard_y, 140,130,self.wizard_frames[self.wiz_frame])

        self.wiz_frame += 1
        self.wiz_frame %= len(self.wizard_frames)

    def balloon_visual(self):
        for i, (x, y, health, balloon_type, _) in enumerate(self.balloon_list):
            color = self.green if health * 100 // self.balloon_health[balloon_type] > 30 else self.red
            balloon_color = self.balloon[balloon_type]
            self.img_center("Balloon", x , y, 40, 64, balloon_color)
            # Vie des ballons
            if health < self.balloon_health[balloon_type]:
                self.rect_full_not_centered(color, x +30 , y - 32, health * 60 // self.balloon_health[balloon_type], 6, 0)
                self.rect_border(self.black, x, y - 35, 60, 6, 1, 0)
            if x > 750:
                self.balloon_list[i] = (x - 1, y, health, balloon_type, _)

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

    def bolt_visual(self):
        for i, (ball_x, ball_y, ball_x_orig, ball_moving) in enumerate(self.bolt_list):
            if ball_moving:
                self.img_center("Dragon_red", ball_x, ball_y, 70, 70, self.bolt[self.bolt_frame])
                self.bolt_frame += 1
                self.bolt_frame %= len(self.fireball)

                ball_x += 15 

                self.bolt_list[i] = (ball_x, ball_y, ball_x_orig, ball_moving)

                if ball_x > ball_x_orig + 500: 
                    self.bolt_list[i] = (ball_x_orig, ball_y, ball_x_orig, False)
                    del self.bolt_list[i]

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
        for i, (balloon_x, balloon_y, health, balloon_type, _) in enumerate(self.balloon_list):
            for j, (ball_x, ball_y, ball_x_orig, status) in enumerate(self.fireballs_list):
                if (balloon_x - 15 <= ball_x <= balloon_x + 15) and (balloon_y - 35 <= ball_y <= balloon_y + 35):
                    if health > self.dragon_damage:
                        self.balloon_list[i] = (balloon_x, balloon_y, health - self.dragon_damage, balloon_type, _)
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
                        if self.entity_moving:
                            self.fireballs_list.append((self.dragon_x, self.dragon_y, self.dragon_x, True))
                        else:
                            self.bolt_list.append((self.wizard_x, self.wizard_y, self.wizard_x, True))
                    if event.key == pygame.K_b:
                        if self.entity_moving:
                            self.entity_moving = False
                        else:
                            self.entity_moving = True
                
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
            if self.entity_moving:
                self.dragon_movement()
            else:
                self.wizard_movement()
            self.dragon_visual()
            self.explosion_visual()
            self.wizard_visual()
            self.balloon_visual()
            self.fireball_visual()
            self.check_target()
            self.update()