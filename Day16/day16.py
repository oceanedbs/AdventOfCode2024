from collections import deque

def read_file_as_2d_array(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

# Example usage
filename = 'Day16/data.txt'
data_2d_array = read_file_as_2d_array(filename)

def print_2d_array(array):
    for row in array:
        print(''.join(row))

# Example usage
print_2d_array(data_2d_array)
    
def find_shortest_path(maze):
        rows, cols = len(maze), len(maze[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        start, end = None, None

        # Find start (S) and end (E) positions
        for r in range(rows):
            for c in range(cols):
                if maze[r][c] == 'S':
                    start = (r, c)
                elif maze[r][c] == 'E':
                    end = (r, c)
        if not start or not end:
            return -1, -1  # No start or end found

        queue = deque([(start[0], start[1], 0, 1, 0)])  # row, col, steps, direction, turns
        visited = set()
        visited.add(start)

        while queue:
            # print(queue)
            r, c, steps, prev_dir, turn = queue.popleft()

            if (r, c) == end:
                return steps, turn  # steps, turns
            
            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    if i==prev_dir:
                        queue.appendleft((nr, nc, steps + 1, i, turn))
                    else:
                        queue.append((nr, nc, steps + 1, i, turn + 1))

        return -1, -1  # No path found

    # Example usage
steps, turns = find_shortest_path(data_2d_array)
print(f"Steps: {steps}, Turns: {turns}")

total_count = steps + 1000*turns
print(f"Total count: {total_count}")