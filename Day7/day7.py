import pandas as pd
from itertools import product

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = []
        for line in file:
            line = line.strip()
            if line:
                data.append([int(x) for x in line.replace(':', ' ').split()])
        return data
    


data = read_data('Day7/data.txt')

operators = ['+', '*', '||']
overall_sum =0

for l in data:
    result = l[0] 
    print(l)
    for ops in product(operators, repeat=len(l[1:])-1):
        total = 0
        expression = str(l[1])
        for num, op in zip(l[2:], ops):
            if op == '||':
                #concatenate integers together
                expression += str(num)
            else :
                expression += f' {op} {num}'
            total = eval(expression)
            expression = str(total)
        if total == l[0]:
           print('Add :', l[0])
           overall_sum += l[0]
           break
print(f"Overall sum is {overall_sum}")

