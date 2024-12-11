import numpy as np

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split()
        return [int(num) for num in data]

data = read_data('Day11/data_test.txt')
print(data)

# Part 1
for i in np.arange(6):
    size = len(data)
    for n in np.arange(size):
        print(data[n])
        if data[n] == 0:
            data[n] = 0
        elif len(str(data[n]))% 2 == 0:
            mid = len(str(data[n])) // 2
            first_half = int(str(data[n])[:mid])
            second_half = int(str(data[n])[mid:])
            data[n] = first_half
            data.insert(n + 1, second_half)
        else:
            data[n] = data[n]*2024
    print(data)

print(len(data))