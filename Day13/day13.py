from sympy import symbols, Eq, solve

def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n\n')
    
    results = []
    for block in data:
        lines = block.split('\n')
        button_a = lines[0].split(': ')[1].split(', ')
        button_b = lines[1].split(': ')[1].split(', ')
        prize = lines[2].split(': ')[1].split(', ')
        
        button_a_x = int(button_a[0].split('+')[1])
        button_a_y = int(button_a[1].split('+')[1])
        button_b_x = int(button_b[0].split('+')[1])
        button_b_y = int(button_b[1].split('+')[1])
        prize_x = int(prize[0].split('=')[1])+10000000000000
        prize_y = int(prize[1].split('=')[1])+10000000000000
        
        results.append({
            'Button A': {'X': button_a_x, 'Y': button_a_y},
            'Button B': {'X': button_b_x, 'Y': button_b_y},
            'Prize': {'X': prize_x, 'Y': prize_y}
        })
    
    return results

# Example usage
file_path = 'Day13/data.txt'
parsed_data = parse_data(file_path)

total_cost = 0

# Part 1
for entry in parsed_data:
    print(entry)
    Ax, Bx = symbols('Ax Bx')

    eq1 = Eq(Ax * entry['Button A']['X'] + Bx * entry['Button B']['X'], entry['Prize']['X'])
    eq2 = Eq(Ax * entry['Button A']['Y'] + Bx * entry['Button B']['Y'], entry['Prize']['Y'])
        
    solution = solve((eq1, eq2), (Ax, Bx))
        
    if solution : #isinstance(solution[Ax], int) and isinstance(solution[Bx], int):
        if solution[Ax].q != 1 or solution[Bx].q != 1:
            print("Solution contains fractions, skipping entry")
            continue
        print(f"Solution for entry: A = {solution[Ax]}, B = {solution[Bx]}")  
        # Compute cost
        cost = abs(solution[Ax])*3 + abs(solution[Bx])*1
        total_cost += cost
    else:
        print("No solution found for entry")

      

print(total_cost)