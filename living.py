import random
from abc import ABC

class Living(ABC):
    def __init__(self, lifetime: tuple[int, int]):
        self.time: int = 0
        self.alive: bool = True
        self.lifetime = random.randint(*lifetime)

    def tictac(self):
        self.time += 1
        if self.time == self.lifetime:
            self.alive = False