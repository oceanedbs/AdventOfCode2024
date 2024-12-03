import pandas as pd 

count_safe = 0

# Read the data
data = []
with open('Day2/data.csv', 'r') as file:
    # Part 1: Process each line of the file
    for line in file:
        data.append(line.strip().split(' '))
        differences = [int(data[-1][i+1]) - int(data[-1][i]) for i in range(len(data[-1])-1)]
        
        # Check if all differences are within the range [-3, 3] and are either all non-negative or all non-positive
        if all(-3 <= diff <= 3 for diff in differences) and (all(diff >= 0 for diff in differences) or all(diff <= 0 for diff in differences)) and all(diff != 0 for diff in differences):
            count_safe += 1
        # Part 2: If the condition is not met, check by removing one element at a time
        else:
            for i in range(len(data[-1])):
                temp_data = data[-1][:i] + data[-1][i+1:]
                differences = [int(temp_data[j+1]) - int(temp_data[j]) for j in range(len(temp_data)-1)]
                if all(-3 <= diff <= 3 for diff in differences) and (all(diff >= 0 for diff in differences) or all(diff <= 0 for diff in differences)) and all(diff != 0 for diff in differences):
                    count_safe += 1
                    break

print(count_safe)