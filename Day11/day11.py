

# Part 1 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def insert_after(self, node, value):
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __len__(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split()
        linked_list = LinkedList()
        for num in data:
            linked_list.append(int(num))
        return linked_list

data = read_data('Day11/data.txt')

# Part 1
for i in range(25):
    print(i)
    added = False
    current = data.head
    while current:
        if added:
            added = False
            current = current.next
            continue
        if current.value == 0:
            current.value = 1
        elif len(str(current.value)) % 2 == 0:
            mid = len(str(current.value)) // 2
            first_half = int(str(current.value)[:mid])
            second_half = int(str(current.value)[mid:])
            current.value = first_half
            data.insert_after(current, second_half)
            added = True
        else:
            current.value = current.value * 2024
        current = current.next

print(len(data))


# Part 2
import numpy as np

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split()
        return [int(num) for num in data]

data = read_data('Day11/data.txt')
print(data)
data_dict = {num: 1 for num in data}
print(data_dict)


for i in range(75):
    print(i)
    keys = list(data_dict.keys())
    new_data_dict = {}
    for i in keys:
            if i == 0:
                if new_data_dict.get(1):
                    new_data_dict[1] += data_dict.pop(i)  
                else:
                    new_data_dict[1] = data_dict.pop(i)
            elif len(str(i)) % 2 == 0:
                mid = len(str(i)) // 2
                first_half = int(str(i)[:mid])
                second_half = int(str(i)[mid:])
                if new_data_dict.get(first_half):
                    new_data_dict[first_half] += data_dict[i]
                else:
                    new_data_dict[first_half]= data_dict[i]
                if new_data_dict.get(second_half):
                    new_data_dict[second_half] += data_dict[i]
                else:
                    new_data_dict[second_half] = data_dict[i]
            else:
                val = 2024*i
                if new_data_dict.get(val):
                    new_data_dict[val] += data_dict.pop(i)
                else:
                    new_data_dict[val] = data_dict.pop(i)
    data_dict = new_data_dict


print(data_dict)
total_sum = sum(data_dict.values())
print(total_sum)
