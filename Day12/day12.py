import numpy as np
import cv2

#open data_test.txt as a 2d array
data = []
with open('Day12/data.txt', 'r') as file:
    for line in file:
        data.append(list(line.strip()))

# Part 1
print(data)

def get_contiguous_regions(data):
    def dfs(x, y, letter, visited):
        if (x < 0 or x >= len(data) or y < 0 or y >= len(data[0]) or 
            (x, y) in visited or data[x][y] != letter):
            return []
        visited.add((x, y))
        region = [(x, y)]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            region.extend(dfs(x + dx, y + dy, letter, visited))
        return region

    visited = set()
    regions = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i, j) not in visited:
                region = dfs(i, j, data[i][j], visited)
                if region:
                    regions.append(region)
    return regions

#get the perimeter size of the region
def get_perimeter(region):
    perimeter = 0
    for i in range(len(region)):
        x, y = region[i]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (x + dx, y + dy) not in region:
                perimeter += 1
    return perimeter


cost =0
regions = get_contiguous_regions(data)
for region in regions:
    print(region)
    perimeter = get_perimeter(region)
    cost += len(region) * perimeter

print(cost)

# Part 2
corner1 = np.array([[0, 0], [0, 1]])
corner2 = np.array([[0, 0], [1, 0]])
corner3 = np.array([[0, 1], [0, 0]])
corner4 = np.array([[1, 0], [0, 0]])
corner_matrix=[corner1, corner2, corner3, corner4]  
    
corner5 = np.array([[1, 1], [1, 0]])
corner6 = np.array([[1, 1], [0, 1]])
corner7 = np.array([[1, 0], [1, 1]])
corner8 = np.array([[0, 1], [1, 1]])
corner_matrix_2=[corner5, corner6, corner7, corner8]  

border_1 = np.array([0, 1])
border_2 = np.array([1, 0])

borders = [border_1, border_2]  
    
def get_corners(region, data):
    corners = 0
    mask = np.zeros(np.array(data).shape,np.uint8)
    for i in range(len(data) - 1):
        for j in range(len(data[0]) - 1):
            submatrix = np.array([[data[i][j], data[i][j+1]], [data[i+1][j], data[i+1][j+1]]])
            for corner in corner_matrix + corner_matrix_2:
                if np.array_equal(submatrix, corner):
                    corners += 1
    # Check for special cases
    for x, y in region:
        if (x == 0 or x == len(data) - 1) and (y == 0 or y == len(data[0]) - 1):
            corners += 1
        else :
            for border in borders:
                if (x == 0 or x == len(data) - 1):
                    if (y + 1 < len(data[0]) and np.array_equal(data[x, y:y+2], border)) or (y - 1 >= 0 and np.array_equal(data[x, y-1:y+1], border)):
                        corners += 1
                if (y == 0 or y == len(data[0]) - 1):
                    if (x + 1 < len(data) and np.array_equal(data[x:x+2, y], border)) or (x - 1 >= 0 and np.array_equal(data[x-1:x+1, y], border)):
                        corners += 1
    return corners


tot_corners = 0
# Example usage of get_corners
for region in regions:
    mask = np.zeros_like(data, dtype=np.uint8)
    for x, y in region:
        mask[x, y] = 1
    for x in range(len(data)):
        for y in range(len(data[0])):
            if (x, y) not in region:
                mask[x, y] = 0
    corners = get_corners(region, mask)
    tot_corners += corners*len(region)

print("Total of corners :", tot_corners)

