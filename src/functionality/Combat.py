from src.entities.Balloon import Balloon
from src.entities.Dragon import Dragon

class Combat:
    def __init__(self):
        self.b = Balloon()
        self.d = Dragon()

        self.explosion_list = []