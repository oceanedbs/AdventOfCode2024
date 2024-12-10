from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt

with open('Day9/data.txt', 'r') as file:
    data = file.read()

print(data)

length = len(data)
# Part 1

i = 0
res = []

for k, char in enumerate(data):
    if k % 2 == 0:
        res.extend([i] * int(char))
        i += 1
    else:
        res.extend(['.'] * int(char))

print(res[0:200])

# Convert the list to a 2D array (heatmap)
# heatmap_size = int(np.ceil(np.sqrt(len(res))))
# heatmap = np.full((heatmap_size, heatmap_size), -1)

# for idx, value in enumerate(res):
#     row = idx // heatmap_size
#     col = idx % heatmap_size
#     heatmap[row, col] = -1 if value == '.' else int(value)

# # Plot the heatmap
# plt.imshow(heatmap, cmap='viridis', interpolation='nearest')
# plt.colorbar()
# plt.title('Heatmap of res')
# plt.show()

last_digit_index = len(res) - 1
for i in range(0, len(res)):
    if res[i] == '.':
        not_placed = True
        while last_digit_index > i and not_placed:
            if isinstance(res[last_digit_index], int):
                res[i] = res[last_digit_index]
                res[last_digit_index] = '.'
                not_placed = False
            last_digit_index -= 1
                
# Convert all integers in res to strings
res = [str(x) for x in res]
result_string = ''.join(res)
print(result_string[0:200])

total=0
for k, char in enumerate(res):
    if(res[k]!='.'):
        total+= int(res[k])*k

print(total)


# # Convert the list to a 2D array (heatmap)
# heatmap_size = int(np.ceil(np.sqrt(len(res))))
# heatmap = np.full((heatmap_size, heatmap_size), -1)

# for idx, value in enumerate(res):
#     row = idx // heatmap_size
#     col = idx % heatmap_size
#     heatmap[row, col] = -1 if value == '.' else int(value)

# # Plot the heatmap
# plt.imshow(heatmap, cmap='viridis', interpolation='nearest')
# plt.colorbar()
# plt.title('Heatmap of res')
# plt.show()

#Part 2


def reconstruct_list(data_blocks) :
    #reconstruct the list based on the data_blocks
    res = ['.'] * ((length*2)+1)
    for db in data_blocks:
        res[db[2]:db[2] + db[1]] = [db[0]] * db[1]
    return res

print('Part 2') 

span_dict = {}

free_spaces_array = np.array(list(map(int, list(data[1::2]))))
print(free_spaces_array)

line_array = list(map(int, list(data)))
print(line_array)

for file_id in range(len(data)-1, -1, -2):
	cur_file_size = int(data[file_id])

	free_spaces = np.argwhere(free_spaces_array[:file_id//2] >= cur_file_size)

	if free_spaces.shape[0] == 0:
		span_start = sum(line_array[:file_id])
		span_dict[file_id//2] = list(range(span_start, span_start + int(data[file_id])))

	else:
		span_start = sum(line_array[:1+free_spaces[0, 0]*2])
		span_dict[file_id//2] = list(range(span_start, span_start + int(data[file_id])))
		free_spaces_array[free_spaces[0, 0]] -= int(data[file_id])
		line_array[free_spaces[0, 0]*2] += int(data[file_id])
		line_array[free_spaces[0, 0]*2 +1] -= int(data[file_id])

		
		
checksum = 0
for key in span_dict:
	checksum += sum([mult * key for mult in span_dict[key]])

print(checksum)