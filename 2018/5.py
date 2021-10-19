#!/usr/bin/env python3

import numpy as np

def main():
    name = input("Specify name (which in-file to be used):")
    file_name = "5_%s.in" % name if name else "5.in"
    with open(file_name, "r") as f:
        polymer = f.readline().strip()
    # Shrink all the way
    reduced_polymer_size = reduce_polymer(polymer)
    # Testremove each unit (not combination-bound), then reduce all the way
    length_list = []
    test_polymer = polymer
    for c in range(ord('A'), ord('Z') + 1):
        test_polymer = test_polymer.replace(chr(c), "").replace(chr(c).lower(), "")
        reduced_test_polymer_size = reduce_polymer(test_polymer)
        length_list.append(reduced_test_polymer_size)
        test_polymer = polymer
    removed_and_reduced_polymer_size = min(length_list)
    # Print the summary
    print("AoC 2018 Day 5: Alchemical Reduction")
    print("  Part 1:")
    print("\tFully reduced polymer length is:", reduced_polymer_size)
    print("  Part 2:")
    print("\tShortest reducable polymer (after unit removal) has length:", removed_and_reduced_polymer_size)

def reduce_polymer(polymer):
    polymer_size = len(polymer)
    shrinking = True
    while shrinking:
        for c in range(ord('A'), ord('Z') + 1):
            counts = True
            while counts:
                polymer = polymer.replace(chr(c) + chr(c).lower(), "").replace(chr(c).lower() + chr(c), "")
                counts = polymer.count(chr(c) + chr(c).lower()) + polymer.count(chr(c).lower() + chr(c))
        new_polymer_size = len(polymer)
        if polymer_size - new_polymer_size == 0:
            shrinking = False
        polymer_size = new_polymer_size
    return new_polymer_size

main()
