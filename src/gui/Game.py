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
        self.score = 0

        self.entity_moving = True # True for Dragon / False for Wizard
        self.dragon_left, self.wizard_left = False, False

        self.img_back = pygame.image.load(f"assets/image/game/background.png").convert_alpha()
        self.img_castle = pygame.image.load(f"assets/image/game/game_castle.png").convert_alpha()
        self.rect_option = pygame.image.load(f"assets/image/game/game_rect.png").convert_alpha()
        self.rect_high_score = pygame.image.load(f"assets/image/game/game_high_score.png").convert_alpha()
        self.crown = pygame.image.load(f"assets/image/game/game_crown.png").convert_alpha()
        self.life = pygame.image.load(f"assets/image/game/game_life.png").convert_alpha()
        self.hp = pygame.image.load(f"assets/image/game/game_hp.png").convert_alpha()


    def background(self):

        # Background
        self.img_background(self.W // 2, self.H // 2, self.W, self.H, self.img_back)

        # Tour
        self.img_not_center("Castle", -90, 115, 375, 515, self.img_castle)

        # Life
        pygame.draw.rect(self.Window, self.black, (1087, 20, 125, 15))
        self.img_not_center("Life", 1060, 15, 160, 26, self.hp)

        # Score
        self.img_not_center("Crown", 75, 5, 35, 35, self.crown)
        self.img_not_center("High Score", 15, 25, 153, 57, self.rect_option)
        self.text_not_center(self.font2, 13, "High Score : 24121993", self.white, 30, 45)

        self.img_not_center("High Score", 15, 75, 153, 57, self.rect_option)
        self.text_not_center(self.font2, 13, f"Your Score : {self.score}", self.white, 30, 95)

       
        # Missile #160
        self.img_txt_hover("Missile","MISSILE", self.W//2-80, 660, 153, 57, self.rect_option, self.rect_option, self.font2, 13, self.white, self.W//2-80, 660)
        if self.bonus_bolt < 5:
            for missile in range(self.bonus_bolt):
                pygame.draw.rect(self.Window, self.red, (485 +30 * missile, 685, 29, 9))
        self.img_not_center("Life", 475, 680, 143, 18, self.life)

        # Double
        self.img_txt_hover("Double","DOUBLE", self.W//2+80, 660, 153, 57, self.rect_option, self.rect_option, self.font2, 13, self.white, self.W//2+80, 660)
        pygame.draw.rect(self.Window, self.black, (645, 685, 120, 9))
        self.img_not_center("Life", 635, 680, 143, 18, self.life)

        # Fireball
        self.img_txt_hover("Fire","FIREBALL", self.W//2+240, 660, 153, 57, self.rect_option, self.rect_option, self.font2, 13, self.white, self.W//2+240, 660)       
        pygame.draw.rect(self.Window, self.black, (805, 685, 120, 9))
        self.img_not_center("Life", 795, 680, 143, 18, self.life)
    
        # Fire range        
        self.img_txt_hover("Fire range","FIRE RANGE", self.W//2-240, 660, 153, 57, self.rect_option, self.rect_option, self.font2, 13, self.white, self.W//2-240, 660)
        pygame.draw.rect(self.Window, self.black, (325, 685, 120, 9))
        self.img_not_center("Life", 315, 680, 143, 18, self.life)
       
    
    def dragon_visual(self):

        if self.dragon_left and self.entity_moving:
            self.img_mirror(self.dragon_x,  self.dragon_y, 177,162,self.red_frames[int(self.dragon_frame)])
        else:
            self.img_center("Dragon_red", self.dragon_x, self.dragon_y, 177,162,self.red_frames[int(self.dragon_frame)])
        # self.img_center("Dragon_black", 700,350,200,200,self.black_frames[int(self.dragon_frame)]) 
        self.dragon_frame += 0.5
        self.dragon_frame %= len(self.red_frames)
        if self.dragon_attack:
            if self.dragon_attack_frame < len(self.fireball):
                self.img_center("Fireball", self.dragon_x +70, self.dragon_y + 5, 6 *self.dragon_attack_frame + self.dragon_attackspeed, 6 *self.dragon_attack_frame + self.dragon_attackspeed, self.fireball[int(self.dragon_attack_frame)])
                self.dragon_attack_frame += self.dragon_attackspeed

            else:
                self.dragon_attack = False
                self.dragon_attack_frame = 0
                self.fireballs_list.append((self.dragon_x +70, self.dragon_y + 5, self.dragon_x +70, True))

    def wizard_visual(self):
        if self.wizard_attack:
            if self.wiz_frame < len(self.wizard_frames):
                self.img_center("Wizard", self.wizard_x, self.wizard_y, 123, 160, self.wizard_frames[int(self.wiz_frame)])
                self.wiz_frame += self.wizard_attack_speed
            else:
                self.wizard_attack = False
                self.wiz_frame %= len(self.wizard_frames)
                if self.bonus_bolt < 5:
                    self.bolt_list.append((self.wizard_x + 45, self.wizard_y - 10, self.wizard_x + 45, True))
                else:
                    for i in range(min(self.bonus_bolt, len(self.bonus_bolt_list))):
                        x, y = self.bonus_bolt_list[i]
                        self.bolt_list.append((self.wizard_x + 45 + x, self.wizard_y - 10 + y, self.wizard_x + 45 + x, True))
                    self.bonus_bolt = 0

        else:
            if self.wizard_left and not self.entity_moving:
                self.img_mirror_wiz(self.wizard_x, self.wizard_y, 123,160,self.wizard_frames[0])
            else:
                self.img_center("Wizard", self.wizard_x, self.wizard_y, 123,160,self.wizard_frames[0])

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
                self.balloon_list[i] = (x - 0.5, y, health, balloon_type, _)

    def fireball_visual(self):
        for i, (ball_x, ball_y, ball_x_orig, ball_moving) in enumerate(self.fireballs_list):
            if ball_moving:
                self.img_center("Dragon_red", ball_x, ball_y, 60, 60, self.fireball[int(self.fireball_frame)])
                self.fireball_frame += 0.5
                self.fireball_frame %= len(self.fireball)

                ball_x += 15 

                self.fireballs_list[i] = (ball_x, ball_y, ball_x_orig, ball_moving)

                if ball_x > ball_x_orig + 200 + self.bonus_range_fireball: 
                    self.fireballs_list[i] = (ball_x_orig, ball_y, ball_x_orig, False)
                    del self.fireballs_list[i]

    def bolt_visual(self):
        for i, (ball_x, ball_y, ball_x_orig, bolt_moving) in enumerate(self.bolt_list):
            if bolt_moving:
                self.img_center("Thunderbolt", ball_x, ball_y, 70, 55, self.thunderbolt)

                ball_x += 15 

                self.bolt_list[i] = (ball_x, ball_y, ball_x_orig, bolt_moving)

                if ball_x > ball_x_orig + 500: 
                    self.bolt_list[i] = (ball_x_orig, ball_y, ball_x_orig, False)
                    del self.bolt_list[i]

    def explosion_visual(self):
        for i, (explo_x, explo_y) in enumerate(self.explosion_list):
                if (explo_x, explo_y) not in self.explosion_frames:
                    self.explosion_frames[(explo_x, explo_y)] = 0
                if self.explosion_frames[(explo_x, explo_y)] < len(self.explosion) - 1:
                    self.img_center("explosion", explo_x, explo_y, 60, 88, self.explosion[int(self.explosion_frames[(explo_x, explo_y)])])
                    self.explosion_frames[(explo_x, explo_y)] += 0.5
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
                        self.score += (10 + self.balloon_health[balloon_type] // 10)
                        del self.balloon_list[i]
                        del self.fireballs_list[j]

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    (self.dragon_y, self.wizard_y)
                    if event.key == pygame.K_DOWN:
                        self.moving_down = True
                    elif event.key == pygame.K_UP:
                        self.moving_up = True
                    elif event.key == pygame.K_RIGHT:
                        self.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.moving_left = True
                        if self.entity_moving:
                            self.dragon_left = True
                        elif not self.entity_moving:
                            self.wizard_left = True
                    if event.key == pygame.K_SPACE:
                        if self.entity_moving:
                            if not self.dragon_attack:
                                self.dragon_attack = True
                            # self.fireballs_list.append((self.dragon_x +70, self.dragon_y + 55, self.dragon_x +70, True)) # Attaque dragon
                        else:
                            if not self.wizard_attack:
                                if self.bonus_bolt < 6: # --------------------
                                    self.bonus_bolt +=1 # A décaler sur les kill des ennemies au sol
                                else:
                                    self.bonus_bolt = 0
                                self.wizard_attack = True

                    if event.key == pygame.K_b:
                        if self.entity_moving:
                            self.entity_moving = False
                        else:
                            self.entity_moving = True
                    if event.key == pygame.K_y: #Test bonus vitesse attaque
                        self.wizard_upgrade(1)
                    elif event.key == pygame.K_r:
                        self.wizard_upgrade(2)
                    elif event.key == pygame.K_t:
                        self.wizard_upgrade(4)
                
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.moving_down = False
                    elif event.key == pygame.K_UP:
                        self.moving_up = False
                    elif event.key == pygame.K_RIGHT:
                        self.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.moving_left = False
                        if self.entity_moving:
                            self.dragon_left = False
                        elif not self.entity_moving:
                            self.wizard_left = False
            if self.entity_moving:
                self.dragon_movement()
            else:
                self.wizard_movement()
                
            self.background()
            self.dragon_visual()
            self.explosion_visual()
            self.wizard_visual()
            self.balloon_visual()
            self.fireball_visual()
            self.bolt_visual()
            self.check_target()
            self.update()