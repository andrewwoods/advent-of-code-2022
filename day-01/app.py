#!/usr/bin/env python3

from pprint import pprint


data_file = "day-01/data.txt"
# Test data - use for debugging
# data_file = "day-01/elf-calories-test-data.txt"

elf_index = 0
elf_total = 0
elves = []

f = open(data_file,"r")

for line in f.readlines():
    print(line, end="")

    if line == "\n":
        elves.append(elf_total) 
        elf_total = 0
    else:
        elf_total += int(line)

elves.append(elf_total)

print("Part 1 result:", max(elves) )

print("Part 2 result:", sum(sorted(elves,reverse=True)[0:3]) )
