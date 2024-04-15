
from src.entities.Balloon import Balloon
from src.entities.Soldier import Soldier

class Enemy(Balloon, Soldier):
    def __init__(self):
        Balloon.__init__(self)
        Soldier.__init__(self)

    def wave(self, bol, niveau):
        if bol:
            self.soldier_creation(niveau)
            self.balloon_creation(niveau)
        return self.ballon_generated, self.soldier_generated
