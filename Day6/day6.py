import numpy as np

#read data as table
def read_data_as_table(file_path):
    with open(file_path, 'r') as file:
        table = [list(line.strip()) for line in file]
    return table

file_path = '/home/dubois/Documents/Autre/AdventOfCode2024/Day6/data_exemple.txt'
table = read_data_as_table(file_path)
print('table size:', len(table), len(table[0]))

# Find the guard position in the table
def find_guard_position(table):
        for i in np.arange(len(table[0])):
            for j in np.arange(len(table[1])):
                if table[i][j] == '^':
                    return (i, j)
        return None

guard_position = find_guard_position(table)
if guard_position:
        print(f"guard found at position: {guard_position}")
else:
        print("guard not found in the table")
        

# set guard displacements
dir = 0
clockwise_directions= [(-1,0), (0,1), (1,0), (0, -1)]
direction =clockwise_directions[dir]

table[guard_position[0]][guard_position[1]] = 'X'

while 0 <= guard_position[0] < len(table) and 0 <= guard_position[1] < len(table[0]):
    j, i= guard_position   
    new_j, new_i =  j + direction[0], i + direction[1]
    if new_i < 0 or new_i >= len(table) or new_j < 0 or new_j >= len(table[0]):
        break
    #if obstacle change direction
    if  table[new_j][new_i] == '#':
        direction = clockwise_directions[(clockwise_directions.index(direction) + 1) % 4]
        new_j, new_i =  j + direction[0], i + direction[1]
    #update guard position
    guard_position = (new_j, new_i)
    print(guard_position)
    #mark the cell as visited'
    table[new_j][new_i] = 'X'

#print table as a matrix
for row in table:
    print(''.join(row))

# Count the number of 'X' in the table
x_count = sum(row.count('X') for row in table)
print(f"Number of cells visited in the table: {x_count}")

# Part 2

obstruction =0
# Part 2: Run through each cell of the table and perform an action
for i in range(len(table)):
    for j in range(len(table[0])):
        found1 = []
        found2 = []
        found3 = []
        if table[i][j] == '#':
            print('found obstacle at', i, j)
            if(j-1 < 0) or i+1 >= len(table):
                #it is not possible to stuck the guard with this obstacle
                continue
            
            # look for possible obstacles position to stuck the guard
            
            # find potential first obstacle (top right corner)
            #look for all cells which x coordinate is greater than actual x 
            #and y coordinate is actual y-1
            for k in range(j+1, len(table[0])):
                if table[i+1][k] == '#':
                    found1.append((i+1, k))
                    print('found1', found1)
                    break
            
            # find potential second obstacle (bottom left corner)
            #look for all cells which x coordinate is  x actual -1
            #and y coordinate is greater than actual y
            for k in range(i+1, len(table)):
                if table[k][j-1] == '#':
                    found2.append((k, j-1))
                    print('found2', found2)
                    break
            if found1 and found2:
                #you can stuck the guard, compute the object position 
                #and update the table
                table[found2[0][0]+1][found1[0][1]-1] = 'O'
                print('obstruction placed at ',  found2[0][0]+1, found1[0][1]-1)
                obstruction +=1
            if found1 and not found2 :
                if(found1[0][1]-1 < 0):
                    #it is not possible to stuck the guard with this obstacle
                    continue
                #search for the third obstacle
                #in the x-1 column of found1 obstacle
                #and y > thant found1 y coordinate
                for k in range(found1[0][0]+1, len(table[0])):
                    if table[k][found1[0][1]-1] == '#':
                        found3.append((k, found1[0][1]-1))
                        print('found3', found3)
                        
                        #place obstruction
                        table[found3[0][0]-1][j-1] = 'O'
                        print('obstruction placed at ',  found3[0][0]-1, j-1)
                        obstruction +=1
                        break
            
            if not found1 and found2:
                if found2[0][0]+1 >= len(table):
                    #it is not possible to stuck the guard with this obstacle
                    continue
                #search for the third obstacle
                #in the x-1 column of found1 obstacle
                #and y > thant found1 y coordinate
                for k in range(found2[0][1]+1, len(table)):
                    print(k)
                    print(found2[0][0]+1)
                    if table[found2[0][0]+1][k] == '#':
                        found3.append((found2[0][0]+1, k))
                        print('found4', found3)
                        
                        #place obstruction
                        table[i+1][found3[0][1]-1] = 'O'
                        print('obstruction placed at ',  i+1, found3[0][1]-1)
                        obstruction +=1
                        break
                
            
# Print the updated table
for row in table:
    print(''.join(row))
    
print('Number of obstructions:', obstruction)