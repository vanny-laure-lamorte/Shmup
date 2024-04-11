import pygame, json

from src.gui.Scenario import Scenario
from src.gui.Option import Option

class Menu (Option, Scenario): 
    def __init__(self):
        Scenario.__init__(self)
        Option.__init__(self)    

        # Option menu
        self.selected_option = 0
        self.selected_nb = 0

        # Player Name
        self.input_name = "ENTER YOUR NAME"

        # Error message
        self.error_length = False
        self.error_no_name = False

        # Info player
        self.add_info_json = False
        self.layer_name = ""

        self.image_paths = {
            "background": "assets/image/Menu/menu_background.jpg",
            "rect_menu": "assets/image/Menu/menu_rect.png",
            "rect_name": "assets/image/Menu/menu_name.png",
            "parchment": "assets/image/Menu/menu_parchment.png",
        }

        self.images = {}
        for name, path in self.image_paths.items():
            self.images[name] = pygame.image.load(path)

    def design_menu(self): 

        # Bakground
        self.img_background(self.W//2, self.H//2, self.W, self.H, self.images["background"])

        # Parchment
        self.img_center("parchment", 900, 400, 450, 550, self.images["parchment"])

        # Title
        self.text_not_center(self.font5, 60,"Elemental Guardians", self.white, 670, 35)
        self.text_not_center(self.font5, 45,"Mage & Wyrm", self.white, 780, 85)

        # Name        
        self.name_rect = self.img_txt_hover_k("name", self.input_name, self.W//2+270, 270, 280, 84, self.images["rect_name"], self.images["rect_name"], self.font2,20, self.white, self.W//2+270,270,0)    

        # Play
        self.play_rect = self.img_txt_hover_k("play", "PLAY",self.W//2+270, 365, 280, 94, self.images["rect_menu"], self.images["rect_menu"], self.font2,20, self.white, self.W//2+270, 365, 1)
    
        # Options
        self.option_rect = self.img_txt_hover_k("options", "OPTIONS",self.W//2+270, 445, 280, 94, self.images["rect_menu"], self.images["rect_menu"], self.font2,20, self.white, self.W//2+270, 445, 2)

        # Exit
        self.exit_rect = self.img_txt_hover_k("exit", "EXIT",self.W//2+270, 525, 280, 94, self.images["rect_menu"], self.images["rect_menu"], self.font2,20, self.white, self.W//2+270, 525, 3)
       
        # Copyright
        self.text_not_center(self.font, 15,"©", self.white, 815, 677)
        self.text_not_center(self.font, 10,"Copyright 2024 | All Rights Reserved ", self.white, 830, 680)

        # Error message: 
            # Lenght
        if self.error_length: 
            self.text_not_center(self.font, 12, "15 characters max", self.red, 850, 283)
        if self.error_no_name: 
            self.text_not_center(self.font, 12, "Please enter your username", self.red, 825, 283)
    
    def save_player_info(self):
            try:
                with open('player_info.json', 'r') as file:
                    data = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = []
            data.append((self.input_name))

            if self.input_name not in data: 
                data.append(self.input_name)

            with open('player_info.json', 'w') as file:
                json.dump(data, file)

    def menu_run (self): 
        self.menu_running = True
        
        while self.menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu_running = False

                elif event.type == pygame.KEYDOWN:

                    # Chose option menu
                    if event.key == pygame.K_UP:
                        if self.selected_option > 0:
                            self.selected_option -= 1
                    elif event.key == pygame.K_DOWN:
                        if self.selected_option < 3 :
                            self.selected_option += 1

                    # Write player name
                    if self.selected_option == 0: 
                        if self.input_name == "ENTER YOUR NAME" and event.unicode :
                            self.input_name = ""

                        if event.key == pygame.K_BACKSPACE :
                            self.input_name = self.input_name[:-1]
                            self.error_length = False
                            self.error_no_name = False
                        else: 
                            if len(self.input_name) < 15:
                                self.input_name += event.unicode
                                self.error_length = False 
                             
                            else:
                                if self.input_name != "ENTER YOUR NAME":
                                    self.error_length = True      

                    if event.key == pygame.K_RETURN:
               
                        if self.selected_option == 1:                           
                            if self.input_name == "" or self.input_name == "ENTER YOUR NAME":
                                self.error_no_name = True
                            else:  
                                self.save_player_info()
                                self.scenario_run()
                                self.menu_running = False

                        elif self.selected_option == 2:
                            self.option_run()
                            self.menu_running = False

                        elif self.selected_option == 3:
                            self.menu_running = False                   

                        elif self.selected_option == 0: 
                            self.error_no_name = False  
          
            self.load_sound("music","src/gui/Man-in-Black-The-Witcher-OST.wav" )

            try:      
                self.play_sound("music", loop=True)
                self.play_sound("music")
                pygame.time.wait(3000)
            finally:
                pass      

            self.design_menu()
            self.update()

