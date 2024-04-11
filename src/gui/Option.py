import pygame
from src.pygame_manager.Element import Element

from src.gui.Game import Game

class Option(Element):
    def __init__(self): 
        Element.__init__(self)
        self.option_running = True
        self.img_back_option = pygame.image.load(f"assets/image/option/option_back.jpg").convert_alpha()
        self.img_map = pygame.image.load(f"assets/image/option/option_map.png").convert_alpha()
        self.img_parchment = pygame.image.load(f"assets/image/option/option_parchment.png").convert_alpha()
        self.img_line= pygame.image.load(f"assets/image/option/option_line.png").convert_alpha()
        self.img_helmet1 = pygame.image.load(f"assets/image/option/option_helmet1.png").convert_alpha()
        self.img_helmet2 = pygame.image.load(f"assets/image/option/option_helmet2.png").convert_alpha()
        self.img_helmet3 = pygame.image.load(f"assets/image/option/option_helmet3.png").convert_alpha()
        self.img_helmet4 = pygame.image.load(f"assets/image/option/option_helmet4.png").convert_alpha()
        self.img_seal= pygame.image.load(f"assets/image/option/option_seal.png").convert_alpha()
        self.img_volume= pygame.image.load(f"assets/image/option/option_volume.png").convert_alpha()
        self.img_mute= pygame.image.load(f"assets/image/option/option_mute.png").convert_alpha()
        self.img_key= pygame.image.load(f"assets/image/option/option_key.png").convert_alpha()
        self.img_check= pygame.image.load(f"assets/image/option/option_check1.png").convert_alpha()
        self.img_check1= pygame.image.load(f"assets/image/option/option_check2.png").convert_alpha()
        self.img_back_menu= pygame.image.load(f"assets/image/option/option_back.png").convert_alpha()
        self.img_arrow= pygame.image.load(f"assets/image/option/option_arrow.png").convert_alpha()
        self.rotation = 0
        self.img_arrow_flip1 = pygame.transform.rotate(self.img_arrow, 90)
        self.img_arrow_flip2 = pygame.transform.rotate(self.img_arrow, -90)
        self.img_arrow_flip3 = pygame.transform.rotate(self.img_arrow, 180)

    def design_option(self):

        # Background
        self.img_background(self.W // 2, self.H // 2, self.W, self.H, self.img_back_option)    

        # Maps
        self.rect_full_opacity(self.grey, 290 , 250, 540, 350, 3, 100)
        self.img_not_center("Map", 40, 90, 500, 318, self.img_map)

        self.rect_full_opacity(self.grey, 290 , 460, 540, 50, 3, 100)
        self.text_not_center(self.font2, 20, "Welcome to Wyrm Empire Lucy ", self.white, 140, 445)

        # Rules
        self.rect_full_opacity(self.grey, 290 , 560, 540, 130, 3, 100)
        self.text_not_center(self.font2, 13, "Your goal is to protect the castle by strategically positioning the dragon and", self.white, 35, 510)
        self.text_not_center(self.font2, 13, "mage to fend off waves of enemies. Use the dragon's fire breath and the mage's", self.white, 35, 525)
        self.text_not_center(self.font2, 13, "spells to defeat foes. Upgrade abilities between waves and deploy special attacks", self.white, 35, 540)
        self.text_not_center(self.font2, 13, "wisely to survive as long as possible.Coordinate your tactics and defend the", self.white, 35, 555)
        self.text_not_center(self.font2, 13, "castle against overwhelming odds to achieve the highest score !", self.white, 35, 570)
        self.text_not_center(self.font2, 13, "Good luck, defender !", self.white, 35, 595)

        # Settings
        self.rect_full_opacity(self.grey, 765 , 350, 390, 550, 3, 100)
        self.text_not_center(self.font2, 20, "Settings", self.white, 730, 90)

        # Option volume
        self.img_txt_hover("Option son1", "Option 1", 650, 170, 30, 30, self.img_check, self.img_check1, self.font, 12, self.white, 695, 170)
        self.img_txt_hover("Option son2", "Option 2", 840, 170, 30, 30, self.img_check, self.img_check1, self.font, 12, self.white, 885, 170)
        self.img_not_center("Volume", 640, 200, 30, 30, self.img_volume)
        self.img_not_center("Mute", 830, 200, 30, 30, self.img_mute)             

        # Option movement
        self.img_txt_hover("Option movement", "Option 1", 650, 270, 30, 30, self.img_check, self.img_check1, self.font, 12, self.white, 695, 270)
        self.img_txt_hover("Option movement ", "Option 2", 840, 270, 30, 30, self.img_check, self.img_check1, self.font, 12, self.white, 885, 270)

        # ZQSD
        self.img_not_center("Z", 650, 320, 30, 30, self.img_key)
        self.text_not_center(self.font, 20, "Z", self.white, 660, 325)
        self.img_not_center("Q", 620, 350, 30, 30, self.img_key)
        self.text_not_center(self.font, 20, "Q", self.white, 630, 355)
        self.img_not_center("S", 650, 350, 30, 30, self.img_key)
        self.text_not_center(self.font, 20, "S", self.white, 660, 355)
        self.img_not_center("D", 680, 350, 30, 30, self.img_key)
        self.text_not_center(self.font, 20, "D", self.white, 690, 355)

        # Directional arrow
        self.img_not_center("Z", 850, 320, 30, 30, self.img_key)
        self.img_not_center("D", 855, 325, 20, 20, self.img_arrow_flip3)
        self.img_not_center("Q", 820, 350, 30, 30, self.img_key)
        self.img_not_center("D", 825, 355, 20, 20, self.img_arrow_flip2)
        self.img_not_center("S", 850, 350, 30, 30, self.img_key)
        self.img_not_center("D", 880, 350, 30, 30, self.img_key)   

        self.img_txt_hover("Option son1", "Option 1", 650, 170, 30, 30, self.img_check, self.img_check1, self.font, 12, self.white, 695, 170)
        self.img_txt_hover("Option son2", "Option 2", 840, 170, 30, 30, self.img_check, self.img_check1, self.font, 12, self.white, 885, 170)

        self.img_txt_hover("Option son1", "Option 1", 650, 270, 30, 30, self.img_check, self.img_check1, self.font, 12, self.white, 695, 270)
        self.img_txt_hover("Option son2", "Option 2", 840, 270, 30, 30, self.img_check, self.img_check1, self.font, 12, self.white, 885, 270)

        # Best player section
        self.img_not_center("parchment", 980, 90, 254, 517, self.img_parchment)
        self.text_not_center(self.font2, 20, "Best players", self.white, 1020, 140)
        self.img_not_center("Seal", 1000, 95, 160, 160, self.img_line)
        self.img_not_center("parchment", 1000, 200, 60, 60, self.img_helmet4)
        self.text_not_center(self.font2, 15, "Lucy Madec", self.white, 1060, 220)
        self.img_not_center("parchment", 1000, 270, 60, 60, self.img_helmet3)
        self.text_not_center(self.font2, 15, "Lucas Martinie", self.white, 1060, 290)
        self.img_not_center("parchment", 1000, 340, 60, 60, self.img_helmet2)
        self.text_not_center(self.font2, 15, "Hamza Naya", self.white, 1060, 360)
        self.img_not_center("parchment", 1000, 410, 60, 60, self.img_helmet1)
        self.text_not_center(self.font2, 15, "Vanny Lamorte", self.white, 1060, 430)

        # Seal
        self.img_not_center("Seal", 1150, 510, 60, 60, self.img_seal)

        # Back to Menu
        self.back_menu = self.img_txt_hover('"back to menu', "MENU", 60, 40, 80, 40 , self.img_back_menu,self.img_back_menu, self.font, 12, self.white, 60, 40)

    def option_run(self):
        while self.option_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.option_running = False

            self.design_option()
            self.update()