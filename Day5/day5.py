from collections import defaultdict, deque

def read_data_rules(file_path):
    data_rules = []
    with open(file_path, 'r') as file:
        for line in file:
            num1, num2 = map(int, line.strip().split('|'))
            data_rules.append((num1, num2))
    return data_rules

def read_data_update(file_path):
    data_update = []
    with open(file_path, 'r') as file:
        for line in file:
            numbers = list(map(int, line.strip().split(',')))
            data_update.append(numbers)
    return data_update


# Update data
file_path = '/home/dubois/Documents/Autre/AdventOfCode2024/Day5/data_rules.txt'
data_rules = read_data_rules(file_path)

update_file_path = '/home/dubois/Documents/Autre/AdventOfCode2024/Day5/data_updates.txt'
data_update = read_data_update(update_file_path)

#Part 1

#Find the updates that do not beak the rules
def find_valid_updates(data_rules, data_update):
    valid_updates = []
    for update in data_update:
        is_valid = True
        for r in data_rules:
            if r[0] in update and r[1] in update:
                if update.index(r[0]) >= update.index(r[1]):
                    is_valid = False
                    break
        if is_valid:
            valid_updates.append(update)
    return valid_updates

# Find the middle page of each valid update, and store it to a list
def find_middle_page(valid_updates):
    middle_pages = []
    for update in valid_updates:
        middle_pages.append(update[len(update) // 2])
    return middle_pages

valid_updates = find_valid_updates(data_rules, data_update)

middle_pages = find_middle_page(valid_updates)

print('Number of valid updates : ', len(valid_updates))
print('List of middle pages : ', middle_pages)
print('Total : ', sum(middle_pages))

#Part 2
#order the updates that are not correct and find their middle page

print('_____ PART 2 ______')

#Remove from data_update the valid updates
def remove_valid_updates(data_update, valid_updates):
    for update in valid_updates:
        data_update.remove(update)
    return data_update


#define the ordering rules
from functools import cmp_to_key

@cmp_to_key
def ordering_rules(a, b):
    if a == b: return 0
    return 1 if (a, b) in data_rules else -1

#Remove the valid updates from the data_update
non_valid_updates = remove_valid_updates(data_update, valid_updates)

#for each non_valid_update, sort it by the ordering_rules
sorted_updates = []
for u in non_valid_updates:
    sorted_updates.append(sorted(u, key=ordering_rules))
    
#Find the middle page of each sorted update
middle_pages = find_middle_page(sorted_updates)
print('Total : ', sum(middle_pages))