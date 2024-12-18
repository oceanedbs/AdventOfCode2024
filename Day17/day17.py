def adv(value):
    global A, B, C
    if value == 4: 
        denom = A
    if value == 5: 
        denom = B
    if value == 6:
        denom = C
    if value == 7:
        print('Not valid')
        return 0
    else:
        denom=value
    A = A // (value ** 2)
    print('updated A:', A)

def bxl(value):
    global A, B, C
    B ^= value

def bst(value):
    global A, B, C
    if value == 4: 
        register = A
    if value == 5:
        register = B
    if value == 6:
        register = C
    B = register & 0b111  # Keep the lowest 3 bits

def jnz(value):
    global A, B, C
    global instruction_pointer
    if A == 0:
        print('A is zero')
        return 1
    else:
        instruction_pointer = value

def bxc(value):
    global A, B, C
    B ^= C
    


def out(value):
    global A, B, C
    if value == 4: 
        register = A
    elif value == 5:
        register = B
    elif value == 6:
        register = C
    else:
        register = value
    print(register %8 & 0b111, end=', ')
    
def bvd(value):
    global A, B, C
    if value == 4: 
        denom = A
    if value == 5: 
        denom = B
    if value == 6:
        denom = C
    if value == 7:
        print('Not valid')
        return 0
    else:
        denom=value
    B = A // (value ** 2)
    
def cdv(value):
    global A, B, C
    if value == 4: 
        denom = A
    if value == 5: 
        denom = B
    if value == 6:
        denom = C
    if value == 7:
        print('Not valid')
        return 0
    else:
        denom=value
    C = A // (value ** 2)
    
# Open and read the data_test.txt file
with open('Day17/data_test.txt', 'r') as file:
    lines = file.readlines()

# Extract register values from the file
A = int(lines[0].split(': ')[1])
B = int(lines[1].split(': ')[1])
C = int(lines[2].split(': ')[1])

print(A, B, C)

# Extract the program instructions from the file
data = list(map(int, lines[4].split(': ')[1].split(',')))
print(data)

# Initialize the instruction pointer
instruction_pointer = 0
    
while instruction_pointer < len(data) and data[instruction_pointer] != -1:
    if data[instruction_pointer] == 0:
        print('adv')
        adv(data[instruction_pointer + 1])
    elif data[instruction_pointer] == 1:
        print('bxl')
        # bxl(data[instruction_pointer + 1])
    elif data[instruction_pointer] == 2:
        print('bst')
        # bst(data[instruction_pointer + 1])
    elif data[instruction_pointer] == 3:
        print('jnz')
        # jnz(data[instruction_pointer + 1])
        # if A != 0:
        #     instruction_pointer -= 2
    elif data[instruction_pointer] == 4:
        print('bxc')
        # bxc(data[instruction_pointer + 1])
    elif data[instruction_pointer] == 5:
        print('out')
        out(data[instruction_pointer + 1])
    elif data[instruction_pointer] == 6:
        print('bvd')
        # bvd(data[instruction_pointer + 1])
    elif data[instruction_pointer] == 7:
        print('cdv')
        # cdv(data[instruction_pointer + 1])
    else:
        print('Not valid')
        break
    instruction_pointer += 2
    print(instruction_pointer)