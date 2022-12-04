#!/usr/bin/env python3

################################################################################
#
# Day 03: Rucksack Reorganization
#
################################################################################

from pprint import pprint
import difflib
import string

############################################################
# Functions
############################################################

def split_in_half(data):
    """TODO: Docstring for split_in_half.
    :returns: array

    Divide the string into 2 equal parts
    """
    n = len(data)

    if n%2 == 0:
        first = data[0:n//2]
        second = data[n//2:]
    else:
        first = data[0:(n//2+1)]
        second = data[(n//2+1):]

    return [first, second]

def compare_strings(left, right):
    """TODO: Docstring for function.

    :left: string
    :right: string
    :returns: string

    """
    d = difflib.Differ()
    diff_result = d.compare(left, right)
    match = ''
    letter = ''
    for item in diff_result:
        if item[0:1] == ' ':
            letter = item.strip()
            if letter not in match:
                match += letter
    return match

def string_union(leftstr, rightstr):
    """TODO: Docstring for string_union.
    :returns: TODO

    """
    result = ''
    for left in leftstr:
        for right in rightstr:
            if left == right and left not in result:
                result += left
    return result

def calc_priority_list():
    """TODO: Docstring for calc_priority_list.

    :returns: list

    """
    score = 1
    priority = {}
    for letter in string.ascii_letters:
       priority[letter] = score
       score += 1

    return priority


############################################################
# Main
############################################################

data_file = "day-03/input.txt"

############
#  Part I  #
############

f = open(data_file,"r")

priorities = calc_priority_list()


# pprint(priorities)
# print('Z=', priorities['Z'])
total_score = 0
for rucksack in f.readlines():
    parts = split_in_half(rucksack.strip())
    diff_result = compare_strings(parts[0], parts[1])
    rucksack_score = priorities[diff_result]
    total_score += rucksack_score

f.close()

print('Part I total_score=', total_score)


#############
#  Part II  #
#############

f = open(data_file,"r")

priorities = calc_priority_list()

total_score = 0
line_count = 0
contents = []
for rucksack in f.readlines():
    line_count += 1
    content = rucksack.strip()
    contents.append(content)

    if line_count == 3:
        result_1 = string_union(contents[0], contents[1])
        result_2 = string_union(contents[0], contents[2])
        result = string_union(result_1, result_2)

        rucksack_score = priorities[result]

        total_score += rucksack_score

        # print('contents=', contents)
        # print('result_1=', result_1, 'result_2=', result_2, 'result=', result)
        # print('rucksack_score', rucksack_score)
        result_1 = ''
        result_2 = ''
        result = ''
        contents = []
        line_count = 0
        rucksack_score = 0
f.close()

print('Part II total_score=', total_score)


