import pygame
from src.gui.Game import Game

class Scenario(Game):
    def __init__(self): 
        Game.__init__(self)

        # Scenario
        self.scenario_running = True
        self.inside_background = pygame.image.load(f"assets/image/scenario/background_inside_castle.jpg").convert_alpha()
        self.scroll_img = pygame.image.load(f"assets/image/scenario/scroll.png").convert_alpha()        
        self.king = pygame.image.load(f"assets/image/scenario/king.png").convert_alpha()
        self.wizard = pygame.image.load(f"assets/image/scenario/wizard.png").convert_alpha()
        self.king_family = pygame.image.load(f"assets/image/scenario/scenario_king_queen.png").convert_alpha() 
        self.knight = pygame.image.load(f"assets/image/scenario/scenario_knight.png").convert_alpha() 

        self.left_char = -100 
        self.right_char = 1450
        self.step = 0

        # Performance
        self.back_p = pygame.image.load(f"assets/image/scenario/scenario_performance.png").convert_alpha()
        self.rect_op= pygame.image.load(f"assets/image/scenario/scenario_card.png").convert_alpha()
        self.back_p = pygame.image.load(f"assets/image/scenario/scenario_performance.png").convert_alpha()
        self.card = pygame.image.load(f"assets/image/scenario/scenario_card.png").convert_alpha()
        self.title = pygame.image.load(f"assets/image/scenario/scenario_title.png").convert_alpha()
        self.bonus1 = pygame.image.load(f"assets/image/scenario/scenario_b1.png").convert_alpha()
        self.bonus2 = pygame.image.load(f"assets/image/scenario/scenario_b2.png").convert_alpha()
        self.bonus3 = pygame.image.load(f"assets/image/scenario/scenario_b3.png").convert_alpha()
        self.selected_perf = 0
        self.selected_perf = 0

    def left_character(self, image):
        if self.left_char < 220:
            self.left_char += 10
        self.img_center("left character", self.left_char, 500, 410, 609, image)

    def right_character(self, image):
        if self.right_char > 1030:
            self.right_char -= 10
        self.img_center("left character", self.right_char, 500, 410, 609, image)

    def right_character_loose(self, image):
        if self.right_char > 1030:
            self.right_char -= 10
        self.img_center("left character", self.right_char, 500, 612, 408, image)

    def first_scenario(self):
        self.right_character(self.king)
        if self.step >= 1: 
            self.left_character(self.wizard)
        self.img_center("scroll", self.W//2, 630, 1100, 180, self.scroll_img)

        if self.right_char == 1030 and self.step == 0:
            self.text_center(self.font4, 30, "Our castle is under attack", self.white, self.W//2, 610)
            self.text_center(self.font4, 30, "Wizard, I command you to defend our land", self.white, self.W//2, 650)
        if self.step == 1 and self.left_char == 220:
            self.text_center(self.font4, 30, "Of course my king", self.white, self.W//2, 630)
            # self.text_center(self.font4, 30, " AUTRE TEXTE, AUTRE TEXTE, AUTRE TEXTE", self.white, self.W//2, 650)
        if self.step == 2:
            self.text_center(self.font4, 30, "Press ENTER to start the game", self.black, self.W//2, 630)

    def win_scenario(self):
        self.right_character(self.king_family)
        if self.step >= 1: 
            self.left_character(self.wizard)
        self.img_center("scroll", self.W//2, 630, 1100, 180, self.scroll_img)

        if self.right_char == 1030 and self.step == 0:
            self.text_center(self.font4, 30, "Good battle!", self.white, self.W//2, 610)
            self.text_center(self.font4, 30, "You have managed to defend the castle and save the princess.", self.white, self.W//2, 650)       

        if self.step == 1:
            self.text_center(self.font4, 30, "Press ENTER to go back to the menu", self.black, self.W//2, 630)

    def loose_scenario(self):
        self.right_character_loose(self.knight)
        if self.step >= 1: 
            self.left_character(self.wizard)
        self.img_center("scroll", self.W//2, 630, 1100, 180, self.scroll_img)

        if self.right_char == 1030 and self.step == 0:
            self.text_center(self.font4, 30, "The enemy has won.", self.white, self.W//2, 610)
            self.text_center(self.font4, 30, "You failed to protect the princess...", self.white, self.W//2, 650)       

        if self.step == 1:
            self.text_center(self.font4, 30, "Press ENTER to go back to the menu", self.black, self.W//2, 630)


    def performance_display(self): 

        # Background bonus
        self.rect_full_opacity(self.grey, self.W//2, self.H//2, 730, 480, 3, 100)
        self.img_center("Back P", self.W//2, self.H//2, 700, 450, self.back_p)
        self.img_center("title", self.W//2, 200, 420, 100, self.title)
        self.text_not_center(self.font, 15,"Choose a permanent bonus for the game", self.brown1, self.W//2-135, self.H//2-160)    

        # Bonus 1
        self.circle(self.yellow, 420, 355, 80)
        self.img_txt_hover_perf("Speed", "Speed", 420, 390, 190, 270, self.card, self.card, self.font1, 12, self.white, 420, self.H//2+115, 1)
        self.img_not_center("Speed", 380, 305, 80, 80, self.bonus1)

        # Bonus 2
        self.circle(self.blue, 620, 355, 80)
        self.img_txt_hover_perf("Attack", "Attack", 620, 390, 190, 270, self.card, self.card, self.font1, 12, self.white, 620, self.H//2+115, 2)
        self.img_not_center("Attack", 580, 305, 80, 80, self.bonus2)

        # Bonus 3
        self.circle(self.brown, 820, 355, 80)
        self.img_txt_hover_perf("Distance", "Distance", 820, 390, 190, 270, self.card, self.card, self.font1, 12, self.white, 820, self.H//2+115, 3)
        self.img_not_center("Distance", 780, 305, 80, 80, self.bonus3)

    def scenario_run(self, input_name):
        while self.scenario_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.scenario_running = False
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        if self.step < 2:
                            self.step += 1

                    elif event.key == pygame.K_RETURN and self.step == 2 :
                        self.game_run(input_name)
                        self.scenario_running = False

                    # Bonus
                    elif event.key == pygame.K_LEFT: 
                        if self.selected_perf > 1:
                            self.selected_perf -= 1
                    elif event.key == pygame.K_RIGHT:
                        if self.selected_perf < 3 :
                            self.selected_perf += 1

                    # elif event.key == pygame.K_RETURN:
                    # #     if self.selected_perf == 1: 
                    # #     if self.selected_perf == 2:
                    # #     if self.selected_perf == 3:     

            self.img_background(self.W // 2, self.H // 2, self.W, self.H, self.inside_background)

            self.first_scenario()
            # self.win_scenario()
            # self.loose_scenario()
            self.performance_display()
            self.update()
