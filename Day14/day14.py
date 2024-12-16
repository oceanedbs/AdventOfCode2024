import numpy as np
import matplotlib.pyplot as plt

size_x = 101
size_y = 103

with open('/home/oceane/Documents/Personel/AdventOfCode2024/Day14/data.txt', 'r') as file:
    data_txt = file.read()
robots = []
for line in data_txt.strip().split('\n'):
    p, v = line.split(' ')
    x, y = map(int, p[2:].split(','))
    vel_x, vel_y = map(int, v[2:].split(','))
    robots.append({'x': x, 'y': y, 'vel_x': vel_x, 'vel_y': vel_y})


grid = [[0 for _ in range(size_x)] for _ in range(size_y)]


def print_grid(grid, robots):
    for r in robots:
        grid[r['y']][r['x']] += 1
    # for row in grid:
    #     print(' '.join(map(str, row)))



for i in range(100):
    for r in robots:
        r['x'] += r['vel_x']
        r['y'] += r['vel_y']
        if 0 >= r['x']  or r['x'] >= size_x:
            r['x'] = r['x']%size_x
        if 0 >= r['y']  or r['y'] >= size_y:
            r['y'] = r['y']%size_y

    print_grid(grid, robots)

    plt.imshow(grid, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.title(f'Heatmap at iteration {i+1}')
    # plt.clim(0, 1)
    plt.show()
    grid = [[0 for _ in range(size_x)] for _ in range(size_y)]


quadrant_counts = [0, 0, 0, 0]

for r in robots:
    if r['x'] != size_x // 2 and r['y'] != size_y // 2:
        if r['x'] < size_x // 2 and r['y'] < size_y // 2:
            quadrant_counts[0] += 1
        elif r['x'] >= size_x // 2 and r['y'] < size_y // 2:
            quadrant_counts[1] += 1
        elif r['x'] < size_x // 2 and r['y'] >= size_y // 2:
            quadrant_counts[2] += 1
        elif r['x'] >= size_x // 2 and r['y'] >= size_y // 2:
            quadrant_counts[3] += 1

print("Quadrant counts:", quadrant_counts)

total = 1
for count in quadrant_counts:
    total *= count

print("Total:", total)
