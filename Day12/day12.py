#open data_test.txt as a 2d array
data = []
with open('Day12/data_test.txt', 'r') as file:
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

def get_corners(region, data):
    corners = 0
    for x, y in region:
        adjacent = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (x + dx, y + dy) in region:
                adjacent += 1
        if adjacent == 2:
            corners += 1
        # Check for outer corners
        if adjacent == 1 or adjacent == 0:
            outer_corners = 0
            for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                if (x + dx < 0 or x + dx >= len(data) or y + dy < 0 or y + dy >= len(data[0]) or (x + dx, y + dy) not in region):
                    outer_corners += 1
            if outer_corners >= 2:
                corners += 1
    return corners

# Example usage of get_corners
for region in regions:
    corners = get_corners(region, data)
    print(f"Region: {region}, Corners: {corners}")
