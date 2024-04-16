import pygame, json
from src.pygame_manager.Element import Element

from src.entities.Dragon import Dragon
from src.entities.Wizard import Wizard
from src.gui.Enemy import Enemy

class Game(Element, Dragon, Wizard, Enemy):
    def __init__(self):
        Element.__init__(self)
        Dragon.__init__(self)
        Wizard.__init__(self)
        Enemy.__init__(self)

        self.game_running = True

        self.explosion_list = []
        self.soldier_death_list = []
        self.score = 0
        self.bol = True
        self.level = 1

        self.entity_moving = True # True for Dragon / False for Wizard
        self.dragon_left, self.wizard_left = False, False

        self.img_back_game = pygame.image.load(f"assets/image/game/background.png").convert_alpha()
        self.img_castle = pygame.image.load(f"assets/image/game/game_castle.png").convert_alpha()
        self.rect_option = pygame.image.load(f"assets/image/game/game_rect.png").convert_alpha()
        self.rect_high_score = pygame.image.load(f"assets/image/game/game_high_score.png").convert_alpha()
        self.crown = pygame.image.load(f"assets/image/game/game_crown.png").convert_alpha()
        self.life = pygame.image.load(f"assets/image/game/game_life.png").convert_alpha()
        self.hp = pygame.image.load(f"assets/image/game/game_hp.png").convert_alpha()
        self.max_hp = 100

        self.balloon_damage = 20 # Damage baloon
        self.soldier_damage = 15

    def background_game(self):

        # Background
        self.img_background(self.W // 2, self.H // 2, self.W, self.H, self.img_back_game)

        # Tour
        self.img_not_center("Castle", -90, 115, 375, 515, self.img_castle)

        # Life
        hp_color = self.limegreen if self.max_hp > 30 else self.red
        pygame.draw.rect(self.Window, self.black, (1087, 20, 125, 15))
        self.img_not_center("Life", 1060, 15, 160, 26, self.hp)
        pygame.draw.rect(self.Window, hp_color, (1087, 20, self.max_hp * 125 // 100, 15))

        with open("player_info.json", "r") as file:
            data = json.load(file)

        sorted_players = sorted(data, key=lambda x: x[1], reverse=True)

        top_score = [score[1] for score in sorted_players[:1]]

        # Score
        self.img_not_center("Crown", 75, 5, 35, 35, self.crown)
        self.img_not_center("High Score", 15, 25, 153, 57, self.rect_option)
        self.text_not_center(self.font2, 13, "High Score : " + str(top_score[0]), self.white, 30, 45)

        self.img_not_center("High Score", 15, 75, 153, 57, self.rect_option)
        self.text_not_center(self.font2, 13, f"Your Score : {self.score}", self.white, 30, 95)

        # Missile #160
        self.img_txt_hover("Missile","MISSILE", self.W//2-80, 660, 153, 57, self.rect_option, self.rect_option, self.font2, 13, self.white, self.W//2-80, 660)
        pygame.draw.rect(self.Window, self.black, (485, 685, 120, 9))
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
        for ult_stack in range(self.ultimate_charge):
            pygame.draw.rect(self.Window, self.red, (805 +12 * ult_stack, 685, 11, 9))
        self.img_not_center("Life", 795, 680, 143, 18, self.life)
        if self.ultimate_visual:
            # self.rect_border(self.white, 867, 690, 124, 10, 2, 5)
            self.img_center("Glowing", self.W//2+240, 657, 215 , 55 ,self.glowing_effect[int(self.glowing_frame)])
            self.glowing_frame += 1
            self.glowing_frame %= len(self.glowing_effect)

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
        self.dragon_frame += 0.4
        self.dragon_frame %= len(self.red_frames)
        if self.dragon_attack:
            if self.dragon_attack_frame < len(self.fireball):
                self.img_center("Fireball", self.dragon_x +75, self.dragon_y + 5, 6 *self.dragon_attack_frame + self.dragon_attackspeed, 6 *self.dragon_attack_frame + self.dragon_attackspeed, self.fireball[int(self.dragon_attack_frame)])
                self.dragon_attack_frame += self.dragon_attackspeed

            else:
                self.dragon_attack = False
                self.dragon_attack_frame = 0
                if self.ultimate_charge < 10 and not self.ultimate:
                    self.ultimate_charge +=1
                if self.ultimate:
                    if self.fireballs_list == []:
                        for i in range(9):
                            self.fireballs_list.append((self.dragon_x +75 + self.ultimate_position[i][0], self.dragon_y + 5+ self.ultimate_position[i][1], self.dragon_x +70 + self.ultimate_position[i][0], True))
                else:
                    self.ultimate_range = 0
                    self.fireballs_list.append((self.dragon_x +75, self.dragon_y + 5, self.dragon_x +70, True))

    # def baby_dragon_visual(self):
    #     for whelp, x, y in self.baby_dragon_list:
    #         self.img_center("Dragon_red", x, y, 177//3 , 162//3 ,self.red_frames[int(self.dragon_frame)])
    #         # self.dragon_frame += 0.4
    #         # self.dragon_frame %= len(self.red_frames)
    #     if self.dragon_attack:
    #         if self.dragon_attack_frame < len(self.fireball):
    #             self.img_center("Fireball", x +25, y + 5 // 3, 6 *self.dragon_attack_frame + self.dragon_attackspeed, 6 self.dragon_attack_frame + self.dragon_attackspeed, self.fireball[int(self.dragon_attack_frame)])
    #             self.dragon_attack_frame += self.dragon_attackspeed
    #         else:
    #             self.whelp_fireballs_list.append((x + 25, y + 5 //3, x + 25, True))

    def wizard_visual(self):
        if self.wizard_attack:
            if self.wiz_frame < len(self.wizard_frames):
                self.img_center("Wizard", self.wizard_x, self.wizard_y, 123, 160, self.wizard_frames[int(self.wiz_frame)])
                self.wiz_frame += self.wizard_attack_speed
            else:
                self.wizard_attack = False
                self.wiz_frame %= len(self.wizard_frames)
                if self.bonus_bolt < 4:
                    self.bolt_list.append((self.wizard_x + 45, self.wizard_y - 10, self.wizard_x + 45, True))
                    self.bonus_bolt +=1 # A décaler sur les kill des ennemies au sol
                else:
                    self.bonus_bolt += 1
                    for i in range(min(self.bonus_bolt, len(self.bonus_bolt_list))):
                        x, y = self.bonus_bolt_list[i]
                        self.bolt_list.append((self.wizard_x + 45 + x, self.wizard_y - 10 + y, self.wizard_x + 45 + x, True))
                    self.bonus_bolt = 0
        else:
            if self.wizard_left and not self.entity_moving:
                self.img_mirror_wiz(self.wizard_x, self.wizard_y, 123,160,self.wizard_frames[0])
            else:
                self.img_center("Wizard", self.wizard_x, self.wizard_y, 123,160,self.wizard_frames[0])

    def soldier_visual(self):
        for i, (x, y, health, soldier_type, _) in enumerate(self.soldier_list):
            color = self.limegreen if health * 100 // self.soldier_health[soldier_type] > 30 else self.red
            frame = self.soldier_frames_walk
            self.img_mirror_sol(x, y, 85 , 105, frame[int(self.soldier_frame)])
            x -= self.soldier_speed
            self.soldier_frame = (self.soldier_frame + self.soldier_frame_speed ) % len(frame)

            if health < self.soldier_health[soldier_type]:
                self.rect_full_not_centered(color, x - 12 , y - 50, health * 60 // self.soldier_health[soldier_type], 6, 0)
                self.rect_border(self.black, x - 40, y - 53, 60, 6, 1, 0)
            if x > 750:
                self.soldier_list[i] = (x - 0.2, y, health, soldier_type, True)
            else:
                self.soldier_list[i] = (x - 0.5, y, health, soldier_type, False)

    def balloon_visual(self):
        for i, (x, y, health, balloon_type, _) in enumerate(self.balloon_list):
            color = self.limegreen if health * 100 // self.balloon_health[balloon_type] > 30 else self.red
            balloon_color = self.balloon[balloon_type]
            self.img_center("Balloon", x , y, 40, 64, balloon_color)
            # Vie des ballons
            if health < self.balloon_health[balloon_type]:
                self.rect_full_not_centered(color, x +30 , y - 32, health * 60 // self.balloon_health[balloon_type], 6, 0)
                self.rect_border(self.black, x, y - 35, 60, 6, 1, 0)
            if x > 750:
                self.balloon_list[i] = (x - 0.5, y, health, balloon_type, True)
            else:
                self.balloon_list[i] = (x - 0.5, y, health, balloon_type, False)


    def fireball_visual(self):
        for i, (ball_x, ball_y, ball_x_orig, ball_moving) in enumerate(self.fireballs_list):
            if ball_moving:
                self.img_center("Dragon_red", ball_x, ball_y, 60, 60, self.fireball[int(self.fireball_frame)])
                self.fireball_frame += 0.5
                self.fireball_frame %= len(self.fireball)

                ball_x += 12

                self.fireballs_list[i] = (ball_x, ball_y, ball_x_orig, ball_moving)

                if ball_x > ball_x_orig + 200 + self.ultimate_range + self.bonus_range_fireball: 
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
                    self.explosion_frames[(explo_x, explo_y)] += 0.15
                else:
                    del self.explosion_list[i]
                    del self.explosion_frames[(explo_x, explo_y)]

    # Death animation for the soldier
    def soldier_death_visual(self):
        for i, (sold_x, sold_y) in enumerate(self.soldier_death_list):
                if (sold_x, sold_y) not in self.soldier_frames:
                    self.soldier_frames[(sold_x, sold_y)] = 0
                if self.soldier_frames[(sold_x, sold_y)] < len(self.soldier_frames_dead) - 1:
                    self.img_mirror_sol(sold_x, sold_y, 85, 105, self.soldier_frames_dead[int(self.soldier_frames[(sold_x, sold_y)])])
                    self.soldier_frames[(sold_x, sold_y)] += 0.16
                else:
                    del self.soldier_death_list[i]
                    del self.soldier_frames[(sold_x, sold_y)]

    def check_target(self):
        castle_rect = pygame.Rect(0, 0, 230, 630)  # Rectangle representing the castle
        for i, (balloon_x, balloon_y, health, balloon_type, _) in enumerate(self.balloon_list):
            for j, (ball_x, ball_y, ball_x_orig, status) in enumerate(self.fireballs_list):
                if (balloon_x - 15 <= ball_x <= balloon_x + 15) and (balloon_y - 35 <= ball_y <= balloon_y + 35):
                    if health > self.dragon_damage:
                        self.balloon_list[i] = (balloon_x, balloon_y, health - self.dragon_damage, balloon_type, _)
                        del self.fireballs_list[j]
                    else:
                        self.explosion_list.append((balloon_x, balloon_y))
                        self.score += (10 + self.balloon_health[balloon_type] // 10)
                        del self.fireballs_list[j]
                        del self.balloon_list[i]

            if balloon_x < 115:
                self.explosion_list.append((balloon_x, balloon_y))
                self.max_hp -= self.balloon_damage
                del self.balloon_list[i]

    # Temporary Check target for the soldier
    def check_target_soldier(self):
        for i, (soldier_x, soldier_y, health, soldier_type, _) in enumerate(self.soldier_list):
            for j, (ball_x, ball_y, ball_x_orig, status) in enumerate(self.bolt_list):
                if (soldier_x - 15 <= ball_x <= soldier_x + 15) and (soldier_y - 35 <= ball_y <= soldier_y + 35):
                    if health > self.wizard_damage:
                        self.soldier_list[i] = (soldier_x, soldier_y, health - self.wizard_damage, soldier_type, _)
                        del self.bolt_list[j]
                    else:
                        self.soldier_death_list.append((soldier_x, soldier_y))
                        self.score += (5 + self.soldier_health[soldier_type] // 10)
                        del self.soldier_list[i]
                        del self.bolt_list[j]

            if soldier_x < 115:
                self.explosion_list.append((soldier_x, soldier_y))
                self.max_hp -= self.soldier_damage
                del self.soldier_list[i]

    # Stop the generation of the enemies
    def set_wave(self):
        if self.ballon_generated > 0 and self.soldier_generated > 0:
            self.bol = False
        return self.bol

    # Check if all enemies died and setting the next wave
    def set_next_wave(self):
        if not self.balloon_list and not self.soldier_list:
            self.bol = True
            self.level += 1
        return self.bol, self.level

    def save_player_info(self, input_name, score):
        if self.level == 2:
            try:
                with open('player_info.json', 'r') as file:
                    data = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = []
            data.append((input_name, score))

            with open('player_info.json', 'w') as file:
                json.dump(data, file)
            self.game_running = False

    def handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
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

                    if event.key == pygame.K_n:
                        if self.entity_moving and not self.ultimate:
                            if not self.dragon_attack:
                                if self.ultimate_charge == 10:
                                    if self.fireballs_list == []:
                                        self.ultimate = True
                                        self.ultimate_visual = True

                    if event.key == pygame.K_SPACE:
                        if self.entity_moving:
                            if not self.dragon_attack:
                                self.dragon_attack = True
                                if self.ultimate:
                                    if self.fireballs_list == []:
                                        self.ultimate_range = 300
                                        self.ultimate_charge = 0
                                        self.ultimate_visual = False
                                        self.dragon_attack = True
                                    else:
                                        self.ultimate = False
                                else:
                                        self.dragon_attack = True
                        else:
                           if not self.wizard_attack:
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

    def update_character_movement(self):
        if self.entity_moving:
            self.dragon_movement()
        else:
            self.wizard_movement()

    def render_game(self):
        self.background_game()
        self.dragon_visual()
        self.fireball_visual()
        self.wizard_visual()
        self.bolt_visual()
        self.explosion_visual()
        self.balloon_visual()
        self.soldier_visual()
        self.soldier_death_visual()

    def game_run(self, input_name):
        while self.game_running:
            self.handle_events()
            self.update_character_movement()
            self.render_game()
            self.wave(self.bol, self.level)
            self.set_wave()
            self.set_next_wave()
            self.check_target()
            self.check_target_soldier()
            self.save_player_info(input_name, self.score)
            self.update()