import pygame
from src.pygame_manager.Element import Element

class Menu (Element): 
    def __init__(self):
        Element.__init__(self)
        pygame.init()

        self.image_paths = {
            "background": "assets/image/Menu/menu_background.jpg",
            "rect_menu": "assets/image/Menu/menu_rect.png",
            "rect_name": "assets/image/Menu/menu_name.png",
            "parchment": "assets/image/Menu/menu_parchment.png",
        }

        self.images = {}
        for name, path in self.image_paths.items():
            self.images[name] = pygame.image.load(path)


    def design(self): 

        # Bakground
        self.img_background(self.W//2, self.H//2, self.W, self.H, self.images["background"])

        # Parchment
        self.img_center("parchment", 900, 400, 450, 550, self.images["parchment"])

        # Title
        self.text_not_center(self.font5, 60,"Elemental Guardians", self.white, 670, 35)
        self.text_not_center(self.font5, 45,"Mage & Wyrm", self.white, 780, 85)

       
        # Copyright
        self.text_not_center(self.font, 15,"©", self.white, 15, 677)
        self.text_not_center(self.font, 10,"Copyright 2024 | All Rights Reserved ", self.white, 30, 680)

    def menu_run (self): 
        self.menu_running = True
        
        while self.menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu_running = False

            self.design()
            self.update()

