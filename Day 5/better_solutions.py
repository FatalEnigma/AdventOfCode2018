import os

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(input_path) as file:
    original_polymer = file.read()


def react(polymer):
    index = -1
    for char in polymer:
        index += 1
        if index != 0:
            if polymer[index-1] == char.swapcase():
                polymer = polymer[:index - 1] + polymer[index + 1:]
                index -= 2
    return polymer


part1 = react(original_polymer)
print "Part 1: Length of polymer after reactions: %s" % len(part1)

part2 = min(((len(react(part1.replace(agent, '').replace(agent.upper(), ''))), agent) for agent in
             set(x.lower() for x in part1)),
            key=lambda x: x[0])
print "Part 2: Minimum length is %d after removing %s/%s" % (part2[0], part2[1].upper(), part2[1])


from functools import reduce


# Bonus solution using reduce
def should_react(x, y):
    return False if not x else x[-1].swapcase() == y


print "Part 1 solved using reduce: %d" % \
      len(reduce((lambda x, y: x[:-1] if should_react(x, y) else x+y), original_polymer))
