import random
import matplotlib.pyplot as plt
from typing import List, Iterator, TypeVar

from host import Host
from virus import Covid19

T = TypeVar('T')
Grid = List[List[List[Host]]]

steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def neighbors(grid: List[List[T]], i: int, j: int) -> Iterator[T]:
    height, width = len(grid), len(grid[0])
    for di, dj in steps:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < height and 0 <= new_j < width:
            yield grid[new_i][new_j]

def get_empty_grid(height: int, width: int) -> Grid:
    return [[[] for _ in range(width)] for _ in range(height)]

def get_virus() -> Covid19:
    return Covid19()

def move(grid: Grid) -> Grid:
    height, width = len(grid), len(grid[0])
    new_grid = get_empty_grid(height, width)

    for i in range(height):
        for j in range(width):
            for host in grid[i][j]:
                di, dj = random.choice(steps)
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < height and 0 <= new_j < width:
                    new_grid[new_i][new_j].append(host)
                else:
                    new_grid[i][j].append(host)
                host.tictac()
    
    return new_grid

def propagate(grid: Grid):
    height, width = len(grid), len(grid[0])

    for i in range(height):
        for j in range(width):
            if all(not host.has(Covid19.name) for host in grid[i][j]):
                continue

            for host in grid[i][j]:
                host.expose(get_virus())
            
            for hosts in neighbors(grid, i, j):
                for host in hosts:
                    host.expose(get_virus())

def count_infected(grid: Grid):
    return sum(
        1
        for row in grid
        for hosts in row
        for host in hosts
        if host.has(Covid19.name)
    )

def main():
    world_size = 30
    population = 300
    initial_infection = 0.2
    probability_of_reinfection = 0.05
    epochs = 150

    grid = get_empty_grid(world_size, world_size)
    for p in range(population):
        i = random.randrange(0, world_size)
        j = random.randrange(0, world_size)
        host = Host.living(probability_of_reinfection)
        if p < initial_infection * population:
            host.infect(get_virus())
        grid[i][j].append(host)

    infected = []
    not_infected = []
    for _ in range(epochs):
        grid = move(grid)
        propagate(grid)
        infected.append(count_infected(grid) / population)
        not_infected.append(1 - infected[-1])

    plt.plot(infected, label="infected")
    plt.plot(not_infected, label="not infected")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()