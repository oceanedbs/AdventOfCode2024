import itertools
from functools import lru_cache



# Open the file data_test.txt
with open('Day19/data.txt', 'r') as file:
    # Read the first line and split by comma to get possible designs
    possible_designs = [design.replace(' ', '') for design in file.readline().strip().split(',')]
    
    # Read the rest of the lines and store them in towels_design
    towels_design = [line.strip() for line in file.readlines()]

# Print the results to verify
print("Possible Designs:", possible_designs)
print("Towels Design:", towels_design)


# Find the maximum string length in towels_design
max_length = max(len(towel) for towel in towels_design)

# Print the maximum string length to verify
print("Maximum String Length in Towels Design:", max_length)
# # Generate all possible combinations of max_length possible designs
# combinations = []
# for i in range(max_length):
#     print(i)
#     combinations += list(itertools.product(possible_designs, repeat=i+1))

# # Concatenate tuples in the list combinations
# concatenated_combinations = [''.join(combination) for combination in combinations]
# # Remove all spaces in the concatenated combinations
# concatenated_combinations = [combination.replace(' ', '') for combination in concatenated_combinations]
@lru_cache(None)
def can_be_created(t, possible_designs):
    if t == "":
        return True
    for design in possible_designs:
        if t.startswith(design):
            if can_be_created(t[len(design):], tuple(possible_designs)):
                return True
    return False 

result = 0
for t in towels_design[1:]:
    print(t)
    if can_be_created(t, tuple(possible_designs)):
        result += 1
        print(f"{t} can be created from possible designs.")
    else:
        print(f"{t} cannot be created from possible designs.")

print(result)


#Part 2

@lru_cache(None)
def is_possible(t, possible_designs):
    if t == "":
        return 1
    count = 0
    for design in possible_designs:
        if t.startswith(design):
            count += is_possible(t[len(design):], tuple(possible_designs))
    return count

result = 0
for t in towels_design[1:]:
    print(t)
    result += is_possible(t, tuple(possible_designs))
print(result)