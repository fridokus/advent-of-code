import numpy as np

# Santa's suit fabric
cols = rows = 1000

with open("3.in", "r") as f:
    fabric = np.zeros((rows, cols), dtype = int)
    original_elfs = []
    original_elf_coordinates = []
    for line in f.readlines():
        elements = line.split()
        elf = elements[0]
        start_col, start_row = list(map(int, elements[2].strip(":").split(",")))
        size_col, size_row =  list(map(int, elements[3].split("x")))
        claim = fabric[start_row:start_row + size_row, start_col:start_col + size_col]
        # Validate if current claim is "original" (no previous claims) in the order of the elves
        if (claim > 0).sum() == 0:
            # Store current elf and claim as "original"
            original_elfs.append(elf)
            original_elf_coordinates.append((start_row, start_row + size_row, start_col, start_col + size_col))
        # Update fabric with current claim
        claim += 1
# Go through the list of elves with "original" claims
for index, elf_coordinates in enumerate(original_elf_coordinates):
    claim = fabric[elf_coordinates[0]:elf_coordinates[1], elf_coordinates[2]:elf_coordinates[3]]
    # Re-check the "original" claims against the updated fabric
    if (claim != 1).sum() == 0:
        # Salvage only the true "original" claim
        the_original_elf = original_elfs[index]

print("AoC Day 3: No Matter How You Slice It")
print("  Part 1:")
print("\tTotal number of elements in fabric:         ", rows * cols)
print("\tTotal number of non-zero elements in fabric:", (fabric > 0).sum())
print("\tTotal number of clashing elements in fabric:", (fabric > 1).sum())
print("  Part 2:")
print("\tThe only elf with no clash of claims:", the_original_elf)
