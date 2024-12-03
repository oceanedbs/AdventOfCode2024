import re

# Open the file 'Day3/data.txt' in read mode
with open('Day3/data.txt', 'r') as file:
    data = file.read()
    
    # Part 1: Find all multiplication instructions and calculate their total sum
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(pattern, data)
    
    total_sum = 0
    for match in matches:
        # Extract the numbers from the match
        numbers = re.findall(r'\d{1,3}', match)
        # Multiply the numbers and add to the total sum
        total_sum += int(numbers[0]) * int(numbers[1])

    print("Total sum:", total_sum)
    
    # Part 2: Filter instructions based on 'don't()' and 'do()' commands as well as the multiplications instructions
    pattern_dont_do = r'don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)'
    matches_dont_do = re.findall(pattern_dont_do, data)
    
    # filter out instructions that follows a don't() command
    filtered_instructions = []
    skip = False
    for instruction in matches_dont_do:
        if instruction == "don't()":
            skip = True
        elif instruction == "do()":
            skip = False
        elif not skip:
            filtered_instructions.append(instruction)
                
    # Calculate the total sum of the filtered instructions
    total_sum = 0
    for match in filtered_instructions:
        numbers = re.findall(r'\d{1,3}', match)
        total_sum += int(numbers[0]) * int(numbers[1])

    print("Total sum filtered:", total_sum)
    