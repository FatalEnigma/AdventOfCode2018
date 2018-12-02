import os

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(input_path) as file:
    parsed_values = [line.strip() for line in file.readlines()]

# Part 1
from collections import Counter

num_appear_twice = 0
num_appear_three_times = 0

for line in parsed_values:
    if 2 in Counter(line).values():
        num_appear_twice += 1
    if 3 in Counter(line).values():
        num_appear_three_times += 1

print "Checksum is: %d" % (num_appear_twice * num_appear_three_times)

# Part 2
from itertools import combinations

for a, b in combinations(parsed_values, 2):
    dis_similar_indexes = [counter for counter, (x, y) in enumerate(zip(a, b)) if x != y]
    if len(dis_similar_indexes) == 1:
        print "Common letters between correct box IDs: %s" % a[:dis_similar_indexes[0]] + a[dis_similar_indexes[0] + 1:]
