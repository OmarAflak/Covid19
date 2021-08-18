from virus import Virus
from system import ImmuneSystem, ImmuneWithProbabilityAfterExposure, ImmuneNot

class Host:
    def __init__(self, immune_system: ImmuneSystem):
        self.immune_system = immune_system
        self.viruses: dict[str, Virus] = dict()

    @property
    def infected(self) -> bool:
        return len(self.viruses) > 0

    def has(self, name: str) -> bool:
        return name in self.viruses
    
    def expose(self, virus: Virus):
        if virus.infect() and self.immune_system.can_be_infected(virus):
            self.infect(virus)
    
    def infect(self, virus: Virus):
        if virus.name not in self.viruses:
            self.viruses[virus.name] = virus

    def tictac(self):
        for virus in self.viruses.values():
            virus.tictac()

        to_remove = []
        for name, virus in self.viruses.items():
            if not virus.alive:
                to_remove.append(name)
                self.immune_system.add_to_memory(virus)
        
        for name in to_remove:
            self.viruses.pop(name)
    
    @classmethod
    def living(cls, probability_of_reinfection: float = 0) -> 'Host':
        return Host(ImmuneWithProbabilityAfterExposure(probability_of_reinfection))
    
    @classmethod
    def matter(cls) -> 'Host':
        return Host(ImmuneNot())