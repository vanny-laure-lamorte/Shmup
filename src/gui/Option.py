import pygame
from src.pygame_manager.Element import Element

class Option(Element):
    def __init__(self): 
        Element.__init__(self)
        self.option_running = True
        self.img_back = pygame.image.load(f"assets/image/option/option_back.jpg").convert_alpha()
        self.img_rect = pygame.image.load(f"assets/image/option/option_rect.png").convert_alpha()
        self.img_map = pygame.image.load(f"assets/image/option/option_map.png").convert_alpha()
        self.img_parchment = pygame.image.load(f"assets/image/option/option_parchment.png").convert_alpha()
        self.img_helmet1 = pygame.image.load(f"assets/image/option/option_helmet1.png").convert_alpha()
        self.img_helmet2 = pygame.image.load(f"assets/image/option/option_helmet2.png").convert_alpha()
        self.img_helmet3 = pygame.image.load(f"assets/image/option/option_helmet3.png").convert_alpha()
        self.img_helmet4 = pygame.image.load(f"assets/image/option/option_helmet4.png").convert_alpha()



    def design(self):

        # Background
        self.img_background(self.W // 2, self.H // 2, self.W, self.H, self.img_back)    

        self.rect_full_opacity(self.grey, 290 , 250, 540, 350, 3, 100)
        self.img_not_center("Map", 40, 90, 500, 318, self.img_map)

        self.rect_full_opacity(self.grey, 290 , 460, 540, 50, 3, 100)
        self.text_not_center(self.font2, 20, "Welcome to Wyrm Empire ", self.white, 150, 445)

        self.rect_full_opacity(self.grey, 290 , 560, 540, 130, 3, 100)
        self.text_not_center(self.font2, 13, "Your goal is to protect the castle by strategically positioning the dragon and", self.white, 35, 510)
        self.text_not_center(self.font2, 13, "mage to fend off waves of enemies. Use the dragon's fire breath and the mage's", self.white, 35, 525)
        self.text_not_center(self.font2, 13, "spells to defeat foes. Upgrade abilities between waves and deploy special attacks", self.white, 35, 540)
        self.text_not_center(self.font2, 13, "wisely to survive as long as possible.Coordinate your tactics and defend the", self.white, 35, 555)
        self.text_not_center(self.font2, 13, "castle against overwhelming odds to achieve the highest score !", self.white, 35, 570)
        self.text_not_center(self.font2, 13, "Good luck, defender !", self.white, 35, 595)


        self.rect_full_opacity(self.grey, 765 , 350, 390, 550, 3, 100)


    def run_option(self):
        while self.option_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.option_running = False

            self.design()
            self.update()