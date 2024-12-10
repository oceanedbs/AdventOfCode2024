with open('Day10/data.txt') as f:
    data = [list(map(int, line.strip())) for line in f]

#Part 1
print(data)

def find_zero_positions(matrix):
    zero_positions = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 0:
                zero_positions.append((i, j))
    return zero_positions

zero_positions = find_zero_positions(data)
print("Zero positions:", zero_positions)

def is_valid_position(x, y):
    return 0 <= x < len(data) and 0 <= y < len(data[0])

def search_path(x, y, value):
    global score
    global reached
    if(value <= 9):
        # Look for adjacent cells with value+1 (4 adjacent cells)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if i== 0 or j == 0:
                    if is_valid_position(x+i, y+j) and data[x+i][y+j] == value + 1:
                        print("Found adjacent cell with value+1 at", x+i, y+j, "with value", data[x+i][y+j])
                        if data[x+i][y+j] == 9 and (x+i, y+j) not in reached:
                            print(score+1)
                            score = score+1
                            reached.append((x+i, y+j))  
                        else:
                            search_path(x+i, y+j, value+1)

score = 0     
for p in zero_positions:
    x, y = p
    reached = []
    print("Checking position", x, y)
    value = data[x][y]
    search_path(x, y, value)
    print("Score : ", score)
    
    
print(score)
    
## Part 2

def search_path(x, y, value):
    global score
    if(value <= 9):
        # Look for adjacent cells with value+1 (4 adjacent cells)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if i== 0 or j == 0:
                    if is_valid_position(x+i, y+j) and data[x+i][y+j] == value + 1:
                        print("Found adjacent cell with value+1 at", x+i, y+j, "with value", data[x+i][y+j])
                        if data[x+i][y+j] == 9 and (x+i, y+j):
                            print(score+1)
                            score = score+1
                        else:
                            search_path(x+i, y+j, value+1)

score = 0     
for p in zero_positions:
    x, y = p
    print("Checking position", x, y)
    value = data[x][y]
    search_path(x, y, value)
    print("Score : ", score)
    
    
print(score)