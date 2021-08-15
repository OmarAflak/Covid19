import random
from typing import Tuple
from living import Living

class Virus(Living):
    name = "unnamed"

    def __init__(self, infection_probability: float, lifetime: Tuple[int, int]):
        super().__init__(lifetime)
        self.infection_probability = infection_probability
    
    def infect(self) -> bool:
        if not self.alive:
            return False
        return random.random() <= self.infection_probability

class Covid19(Virus):
    name = "Covid19"

    def __init__(self):
        super().__init__(0.5, (15, 30))