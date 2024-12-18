
import matplotlib.pyplot as plt

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def parse_content(content):
    parts = content.split('\n\n')
    grid_part = parts[0]
    rules_part = parts[1]
    
    grid = [list(line) for line in grid_part.split('\n')]
    rules = rules_part.split('\n')
    rules = ''.join(rules)
    
    
    return grid, rules

def print_grid(at_position, walls, objects):
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if (x, y) == at_position:
                print('@', end='')
            elif (x, y) in walls:
                print('#', end='')
            elif (x, y) in objects:
                print('O', end='')
            else:
                print('.', end='')
        print()

def plot_grid(at_position, walls, objects, rule, next_rule):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xticks(range(len(grid[0])))
    ax.set_yticks(range(len(grid)))
    ax.grid(True)

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if (x, y) == at_position:
                ax.plot(x, y, 'go')  # Green for the current position
            elif (x, y) in walls:
                ax.plot(x, y, 'rs')  # Red squares for walls
            elif (x, y) in objects:
                ax.plot(x, y, 'bo')  # Blue circles for objects
            else:
                ax.plot(x, y, 'w.')  # White dots for empty spaces
    ax.set_title(f"Current Instruction: {rule}, Next Instruction: {next_rule}")

    plt.gca().invert_yaxis()
    plt.show()


if __name__ == "__main__":
    file_path = 'Day15/data_test.txt'
    content = read_file(file_path)
    grid, rules = parse_content(content)
    
    print("Grid:")
    for row in grid:
        print(''.join(row))
    
    print("\nRules:")
    print(rules)

    at_position = None
    walls = set()
    objects = set()
    
  

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '@':
                at_position = (x, y)
            elif char == '#':
                walls.add((x, y))
            elif char == 'O':
                objects.add((x, y))

    print("\n@ Position:", at_position)
    print("Walls:", walls)
    print("Objects:", objects)

    for i, rule in enumerate(rules):
        print(rule)
        if rule == '^':
            dir=(0, -1)
        elif rule == 'v':
            dir=(0, 1)
        elif rule == '<':
            dir=(-1, 0) 
        elif rule == '>':
            dir=(1, 0)
        
        # print("Direction:", dir)
        new_position = (at_position[0] + dir[0], at_position[1] + dir[1])
        # print("New Position:", new_position)
        if new_position in walls:
            # print("Wall : reset previous position")
            new_position = at_position

        elif new_position in objects:
            empty_found = False
            temp_position = new_position
            while 0 <= temp_position[0] < len(grid[0]) and 0 <= temp_position[1] < len(grid) and temp_position not in walls:
                if temp_position not in walls and temp_position not in objects:
                    empty_found = True
                    break
                temp_position = (temp_position[0] + dir[0], temp_position[1] + dir[1])
            
            if empty_found:
                # print("Empty space found, shifting objects")
                #objects.remove(new_position)
                while temp_position != new_position:
                    prev_position = (temp_position[0] - dir[0], temp_position[1] - dir[1])
                    objects.add(temp_position)
                    objects.remove(prev_position)
                    temp_position = prev_position
                at_position = new_position
            else:
                continue
                # print("No empty space found, cannot move")
            
        else:
            # print("Empty, move ok")
            at_position = new_position
        
        # print('Position :', at_position)
        # print('Objects :', objects)
        # print_grid(at_position, walls, objects)
        # plot_grid(at_position, walls, objects, rule, rules[i+1] if i+1 < len(rules) else 'End')


    cost =0

    for o in objects:
        cost += o[0]+ 100*o[1]
    
    print("Cost:", cost)


## Part 2

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '@':
                at_position = (x, y)
            elif char == '#':
                walls.add((x, y))
                walls.add((x+1, y+1))
            elif char == 'O':
                objects.add((x, y))