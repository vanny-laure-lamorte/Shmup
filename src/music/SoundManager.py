import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {} 

    def load_sound(self, name, file_path):
        try:
            sound = pygame.mixer.Sound(file_path)
            self.sounds[name] = sound
        except pygame.error as e:
            print(f"Error loading sound ({name}): {e}")

    def play_sound(self, name, loop=False):
        try:
            sound = self.sounds[name]
            sound.play(-1 if loop else 0) 
        except KeyError:
            print(f"Sound not found ({name})")

    def stop_sound(self, name):
        if name in self.sounds:
            self.sounds[name].stop()
        else:
            print(f"Sound not found ({name})")

    def stop_all_sounds(self):
        pygame.mixer.stop()
