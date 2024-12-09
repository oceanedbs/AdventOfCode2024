from operator import itemgetter

with open('Day9/data_test.txt', 'r') as file:
    data = file.read()

print(data)

# Part 1

i = 0
res = []

for k, char in enumerate(data):
    if k % 2 == 0:
        res.extend([i] * int(char))
        i += 1
    else:
        res.extend(['.'] * int(char))

print(res[0:100])



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


#Part 2


def reconstruct_list(data_blocks) :
    #reconstruct the list based on the data_blocks
    res = ['.'] * len(data)
    for db in data_blocks:
        res[db[2]:db[2] + db[1]] = [db[0]] * db[1]
    return res

print('Part 2') 
i = 0
res = []
data_blocks = []
data_blanks = []
for k, char in enumerate(data):
    size = len(res)
    if k % 2 == 0:
        res.extend([i] * int(char))
        data_blocks.append([i, int(char), size])        
        i += 1

    else:
        res.extend(['.'] * int(char))
        data_blanks.append([int(char), size])
print(res)

print('blanks : ', data_blanks)
print('blocks : ', data_blocks)

for db in reversed(data_blocks):
    for b in data_blanks:
        if db[1] <= b[0]:
            print('Change block', db, 'to blank', b)
            db[2] = b[1]
            b[0] = b[0] - db[1]
            data_blocks = sorted(data_blocks, key=itemgetter(2))
            print('Sorted blocks : ', data_blocks)
            print(reconstruct_list(data_blocks))
            break
            

print('blanks : ', data_blanks)
print('blocks : ', data_blocks)


