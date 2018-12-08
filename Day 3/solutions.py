import os
import re
from collections import defaultdict

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(input_path) as file:
    regex = re.compile(r'#(?P<id>\d+)\s@\s(?P<x>\d+),(?P<y>\d+):\s(?P<width>\d+)x(?P<height>\d+)')
    parsed_values = {int(re.match(regex, line).group('id')): {x: int(y)
                                                              for x, y in re.match(regex, line).groupdict().iteritems()
                                                              if x != 'id'} for line in file.readlines()}

# Part 1 & 2 Combined
grid = defaultdict(lambda: [int(), list()])
overlaps = {key: False for key in parsed_values}

for claim, data in parsed_values.iteritems():
    for x in xrange(data['x'], data['x'] + data['width']):
        for y in xrange(data['y'], data['y'] + data['height']):
            if grid[(x, y)][0] >= 1:
                overlaps[claim] = True
                for existing_ids in grid[(x, y)][1]:
                    overlaps[existing_ids] = True
            grid[(x, y)][0] = grid[(x, y)][0] + 1
            grid[(x, y)][1].append(claim)

print "Square inches of at least 2 claims: %d" % sum(x[0] >= 2 for x in grid.values())
print "ID with no overlaps: %d " % (x for x, y in overlaps.iteritems() if not y).next()
