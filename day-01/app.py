#!/usr/bin/env python3

from pprint import pprint


data_file = "day-01/data.txt"
data_file = "day-01/elf-calories-test-data.txt"

elf_index = 0
elf_total = 0
elf_max = 0
baller_elf = 0
grand_total = 0
elves = []

f = open(data_file,"r")
lines = f.readlines()

for line in lines:
    print(line, end="")

    if line == "\n":

        if elf_total > elf_max:
            elf_max = elf_total
            baller_elf = elf_index

        elves.append(elf_total) 
        grand_total += elf_total

        # Reset values
        elf_total = 0
        elf_index += 1
        continue

    elf_total += int(line)

if elf_total > elf_max:
    elf_max = elf_total
    baller_elf = elf_index

elves.append(elf_total)
grand_total += elf_total

print("Elf Total=", elf_total, "\n", end="")
print("Baller Elf=", baller_elf, "\n", end="")
print("Grand Total=", grand_total, "\n", end="")

