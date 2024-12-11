import numpy as np

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split()
        return [int(num) for num in data]

data = read_data('Day11/data.txt')
print(data)

# Part 1
for i in np.arange(25):
    added = False
    for p in data:
        if added == True:
            added = False
            continue
        if p == 0:
            data[data.index(p)] = 1
        elif len(str(p))% 2 == 0:
            mid = len(str(p)) // 2
            first_half = int(str(p)[:mid])
            second_half = int(str(p)[mid:])
            data[data.index(p)] = first_half
            data.insert(data.index(first_half) + 1, second_half)
            added = True
        else:
            data[data.index(p)]= p*2024

print(len(data))