import random
from typing import Dict
from collections import defaultdict
from abc import ABC, abstractmethod
from virus import Virus

class ImmuneSystem(ABC):
    def __init__(self):
        self.memory: Dict[str, int] = defaultdict(int)
    
    def add_to_memory(self, virus: Virus):
        self.memory[virus.name] +=1
    
    @abstractmethod
    def can_be_infected(self, virus: Virus) -> bool:
        pass

class ImmuneNot(ImmuneSystem):
    def can_be_infected(self, virus: Virus) -> bool:
        return True

class ImmuneWithProbabilityAfterExposure(ImmuneSystem):
    def __init__(self, probability_of_reinfection: float):
        super().__init__()
        self.probability_of_reinfection = probability_of_reinfection

    def can_be_infected(self, virus: Virus) -> bool:
        if virus.name not in self.memory:
            return True
        return random.random() < self.probability_of_reinfection

class ImmuneAfterSingleExposure(ImmuneWithProbabilityAfterExposure):
    def __init__(self):
        super().__init__(0)