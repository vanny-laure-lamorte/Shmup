import pygame
from src.pygame_manager.Screen import Screen
class Element(Screen):
    def __init__(self):
        Screen.__init__(self)

        # Color
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        # Font

        self.font1 = "assets/font/Roboto-Black.ttf"
      

# Def text
    def text_center(self, font, text_size, text_content, color, x, y):
        pygame.font.init()
        text = pygame.font.Font(f"{font}", text_size).render(text_content, True,color)
        text_rect = text.get_rect(center=(x, y))
        self.Window.blit(text, text_rect)
    
    def text_not_center(self, font, text_size, text_content, color, x, y):
        text = pygame.font.Font(f"{font}", text_size).render(text_content, True, color)
        text_rect = text.get_rect(topleft=(x, y))
        self.Window.blit(text, text_rect)

    def text_center_italic(self, font, text_size, text_content, color, x, y):
        pygame.font.init()
        font_obj = pygame.font.Font(f"{font}", text_size)
        text = font_obj.render(text_content, True, color)
        text_rect = text.get_rect(center=(x, y))
        self.Window.blit(text, text_rect)

# Def image

    def img_center(self, name, x, y, width, height, image):
        name = pygame.transform.smoothscale(image, (width, height))
        self.Window.blit(name, (x - name.get_width()//2, y - name.get_height()//2))
        button = pygame.Rect((x - width//2), (y - height//2), width, height)
        return button

    # Mines weeper - Tom and Jerry Logo
    def img_not_center(self, name, x, y, width, height, image):
        name = pygame.transform.smoothscale(image,(width,height))
        self.Window.blit(name, (x,y))
        button = pygame.Rect(x, y, width, height)
        return button
        
    def img_background(self, x, y, width, height, image):
        image = pygame.transform.smoothscale(image, (width, height))
        self.Window.blit(image, (x - image.get_width()//2, y - image.get_height()//2))

    def img_hover(self, name_rect, name, x, y, width, height, image_name, image_name_hover): 
        name_rect = pygame.Rect( x - width//2, y - height//2, width, height)        
        if self.is_mouse_over_button(name_rect):
            self.img_center(name, x, y, width+5, height+5, image_name_hover)     
        else:
            self.img_center(name, x, y, width, height, image_name)
        return name_rect
    
    def img_txt_hover(self, name_rect, txt, x, y, width, height, image_name, image_name_hover, font, txt_size, color, x_t, y_t): 
        name_rect = pygame.Rect( x - width//2, y - height//2, width + len(txt)*txt_size, height)   
        self.text_not_center(font, txt_size, txt, color, x_t, y_t)
        if self.is_mouse_over_button(name_rect):
            self.img_center(txt, x, y, width+5, height+5, image_name_hover)     
        else:
            self.img_center(txt, x, y, width, height, image_name)

        return name_rect
    

# Def rectangle  
    def rect_full(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width//2, y - height//2, width, height),0, radius)
        return button    
      
    def rect_full_not_centered(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width, y - height, width, height),0, radius)
        return button

    def rect_border(self, color, x, y, width, height, thickness, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width //2, y - height //2, width, height),  thickness, radius)
        return button
    
    # Rect border only on top  
    def rect_radius_top(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width //2, y - height //2, width, height),False,0, radius, radius)
        return button


# # Def Circle
#     def circle(self, color, x, y, radius):
#         pygame.draw.circle(self.Window, color, (x,y), radius)

#     def circle_alpha(self, alpha_color, x, y, radius):
#         circle_surface = pygame.Surface((self.W,self.H), pygame.SRCALPHA)
#         pygame.draw.circle(circle_surface,alpha_color,(x,y),radius)
#         self.Window.blit(circle_surface, (0,0))

#     def circle_hover(self, name, color,alpha_color, x, y, radius): 
#         name = pygame.draw.circle(self.Window, color, (x,y), radius)

#         if self.is_mouse_over_button(name):
#             self.circle_alpha(alpha_color, x, y, radius)
#         else:
#             self.circle(color, x, y, radius)

# Def Hover
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)
    
    def button_hover(self, name, x, y, width, height, color_full, color_border, color_hover, color_border_hover, text, font, text_color,text_size, thickness, radius): 

        name = pygame.Rect((x - width//2), (y - height//2), width, height)

        if self.is_mouse_over_button(name):
            self.rect_full(color_hover, x, y, width + 5, height + 5, radius)
            self.rect_border(color_border_hover, x, y, width + 5, height + 5, thickness, radius)
        else:
            self.rect_full(color_full, x, y, width, height, radius)
            self.rect_border(color_border, x, y, width, height, thickness, radius)
        self.text_center(font, text_size, text, text_color,  x, y)

        return name   

    def button_hover_small(self, name, x, y, width, height, color_full, color_border, color_hover, color_border_hover, text, font, text_color,text_size, thickness, radius): 

        name = pygame.Rect((x - width//2), (y - height//2), width, height)

        if self.is_mouse_over_button(name):
            self.rect_full(color_hover, x, y, width + 3, height + 3, radius)
            self.rect_border(color_border_hover, x, y, width + 3, height + 3, thickness, radius)
        else:
            self.rect_full(color_full, x, y, width, height, radius)
            self.rect_border(color_border, x, y, width, height, thickness, radius)
        self.text_center(font, text_size, text, text_color,  x, y)

        return name     
 
