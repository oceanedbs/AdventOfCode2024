from itertools import combinations

def read_table(file_path):
    table = []
    with open(file_path, 'r') as file:
        for line in file:
            table.append([char for char in line.strip()])
    return table

file_path = 'Day8/data.txt'
table = read_table(file_path)

def print_table(table):
    for row in table:
        print(row)

print_table(table)

#Part 1

letter_positions = {}

for y, row in enumerate(table):
    for x, char in enumerate(row):
        if char == '.':
            continue
        if char not in letter_positions:
            letter_positions[char] = []
        letter_positions[char].append((x, y))

print(letter_positions)

for letter in letter_positions.keys():
    for pos1, pos2 in combinations(letter_positions[letter], 2):
        dx = pos2[0] - pos1[0]
        dy = pos2[1] - pos1[1]
        if 0 <= pos1[1] - dy < len(table) and 0 <= pos1[0] - dx < len(table[0]):
            table[pos1[1] - dy][pos1[0] - dx] = '#'
        if 0 <= pos2[1] + dy < len(table) and 0 <= pos2[0] + dx < len(table[0]):
            table[pos2[1] + dy][pos2[0] + dx] = '#'
        
print_table(table)

# Count the number of '#'
count_hash = sum(row.count('#') for row in table)
print(f"Number of '#': {count_hash}")


#Part 2
table = read_table(file_path)

print_table(table)

print('Part 2')
for letter in letter_positions.keys():
    for pos1, pos2 in combinations(letter_positions[letter], 2):
        dx = pos2[0] - pos1[0]
        dy = pos2[1] - pos1[1]
        #find the highest common factor of dx and dy
        factor = 1
        for i in range(2, min(abs(dx), abs(dy)) + 1):
            if dx % i == 0 and dy % i == 0:
                factor = i
        dx //= factor
        dy //= factor
        x, y = pos1
        while 0 <= x < len(table[0]) and 0 <= y < len(table):
            table[y][x] = '#'
            x += dx
            y += dy
        x,y = pos2
        while 0 <= x < len(table[0]) and 0 <= y < len(table):
            table[y][x] = '#'
            x -= dx
            y -= dy
print_table(table)


count_hash = sum(row.count('#') for row in table)
print(f"Number of '#': {count_hash}")
