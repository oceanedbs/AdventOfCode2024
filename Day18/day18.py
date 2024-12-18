from collections import deque



size_array = 71


with open('Day18/data.txt', 'r') as file:
    data_txt = [tuple(map(int, line.strip().split(','))) for line in file]
    
n_byte_to_consider = 1024
print(data_txt)

array_2d = [[0] * size_array for _ in range(size_array)]
print(array_2d)

def print_2d_array(array):
    for row in array:
        print(''.join(str(row))) 

for n in range(n_byte_to_consider):
    x, y = data_txt[n]
    array_2d[y][x] = '#'

print_2d_array(array_2d)

def is_valid_move(x, y, array):
    return 0 <= x < size_array and 0 <= y < size_array and array[y][x] != '#'

def bfs_shortest_path(array, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) == goal:
            return path
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_x, next_y = x + dx, y + dy
            if is_valid_move(next_x, next_y, array) and (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                queue.append(((next_x, next_y), path + [(next_x, next_y)]))
    
    return None

start = (0, 0)
goal = (size_array - 1, size_array - 1)
path = bfs_shortest_path(array_2d, start, goal)

if path:
    print("Shortest path:", path)
    print(len(path)-1)
else:
    print("No path found")
    
# Part 2
array_2d = [[0] * size_array for _ in range(size_array)]
for n in range(len(data_txt)):
    x, y = data_txt[n]
    array_2d[y][x] = '#'
    path = bfs_shortest_path(array_2d, start, goal)
    if path:
        print("Shortest path:", len(path)-1)
    else:
        print("No path found")
        break
    
print("number of bytes to consider:", n, "coordinates:", x, y)    
