import os

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(input_path) as file:
    parsed_values = [int(line.strip()) for line in file.readlines()]

# Part 1
print "Part 1: %d" % sum(parsed_values)

# Part 2
from itertools import cycle

seen = ({0})
current_value = 0

for value in cycle(parsed_values):
    value = int(value)
    current_value += value
    if current_value in seen:
        print "Part 2: %d" % current_value
        break
    seen.add(current_value)
