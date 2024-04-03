import pygame

class Screen:
    def __init__(self):
        pygame.init()
        self.W = 1000
        self.H = 700
        self.Window = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Budget Buddy")
        pygame.display.set_icon(pygame.image.load("assets/image/icon.png"))
        self.clock = pygame.time.Clock()

    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(30)
        self.Window.fill((0, 0, 0))

    def screen_color(self, color): 
        self.Window.fill(color)
