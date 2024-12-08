import pandas as pd
from itertools import product

# Function to read data from a file and process it into a list of lists of integers
def read_data(file_path):
    with open(file_path, 'r') as file:
        data = []
        for line in file:
            line = line.strip()
            if line:
                data.append([int(x) for x in line.replace(':', ' ').split()])
        return data

# Read data from the specified file
data = read_data('Day7/data.txt')

# Define the operators to be used in the expressions
operators = ['+', '*', '||']
overall_sum = 0

# Iterate over each list in the data
for l in data:
    result = l[0]  # The target result to match
    print(l)
    # Generate all possible combinations of operators
    for ops in product(operators, repeat=len(l[1:])-1):
        total = 0
        expression = str(l[1])
        # Build and evaluate the expression using the current combination of operators
        for num, op in zip(l[2:], ops):
            if op == '||':
                # Concatenate integers together
                expression += str(num)
            else:
                expression += f' {op} {num}'
            total = eval(expression)
            expression = str(total)
        # Check if the evaluated total matches the target result
        if total == l[0]:
            print('Add :', l[0])
            overall_sum += l[0]
            break

# Print the overall sum of all matching results
print(f"Overall sum is {overall_sum}")
