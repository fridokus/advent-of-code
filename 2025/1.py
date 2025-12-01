import re

def solve_part1(input_data):
    """
    Part 1 Logic:
    Only checks if the dial lands on 0 at the very END of the rotation.
    """
    current_pos = 50
    zero_count = 0
    instructions = re.findall(r'([LR])(\d+)', input_data)

    for direction, value in instructions:
        amount = int(value)
        if direction == 'L':
            current_pos = (current_pos - amount) % 100
        elif direction == 'R':
            current_pos = (current_pos + amount) % 100

        if current_pos == 0:
            zero_count += 1

    return zero_count

def solve_part2(input_data):
    """
    Part 2 Logic:
    Simulates the rotation step-by-step.
    Counts +1 every single time the dial touches 0 DURING or AT THE END of a rotation.
    """
    current_pos = 50
    total_zeros = 0
    instructions = re.findall(r'([LR])(\d+)', input_data)

    for direction, value in instructions:
        steps = int(value)

        # We simulate 1 click at a time to catch every '0'
        # This handles large loops (e.g. R1000) correctly
        for _ in range(steps):
            if direction == 'L':
                current_pos = (current_pos - 1) % 100
            else: # 'R'
                current_pos = (current_pos + 1) % 100

            # Check every single click
            if current_pos == 0:
                total_zeros += 1

    return total_zeros

# Read the file
with open('1.in', 'r') as f:
    full_input = f.read()

# Calculate and Print Results
p1_answer = solve_part1(full_input)
p2_answer = solve_part2(full_input)

print(f"Part 1 Password: {p1_answer}")
print(f"Part 2 Password: {p2_answer}")
