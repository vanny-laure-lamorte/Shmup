import pygame
from src.gui.Game import Game

class Scenario(Game):
    def __init__(self): 
        Game.__init__(self)

        self.scenario_running = True
        self.inside_background = pygame.image.load(f"assets/image/scenario/background_inside_castle.jpg").convert_alpha()
        self.scroll_img = pygame.image.load(f"assets/image/scenario/scroll.png").convert_alpha()
        
        self.king = pygame.image.load(f"assets/image/scenario/king.png").convert_alpha()
        self.wizard = pygame.image.load(f"assets/image/scenario/wizard.png").convert_alpha()
        
        self.left_char = -100 
        self.right_char = 1450
        self.step = 0

    def left_character(self, image):
        if self.left_char < 220:
            self.left_char += 10
        self.img_center("left character", self.left_char, 500, 410, 609, image)
        
    def right_character(self, image):
        if self.right_char > 1030:
            self.right_char -= 10
        self.img_center("left character", self.right_char, 500, 410, 609, image)

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

    def scenario_run(self):
        while self.scenario_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.scenario_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.step < 2:
                            self.step += 1
                
                    elif event.key == pygame.K_RETURN and self.step == 2 :
                        self.game_run()
                        self.scenario_running = False

            self.img_background(self.W // 2, self.H // 2, self.W, self.H, self.inside_background)
            self.first_scenario()
            self.update()
