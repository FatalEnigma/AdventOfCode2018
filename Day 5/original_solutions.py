import os

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(input_path) as file:
    original_polymer = file.read()


def react(polymer):
    reactions = True

    while reactions:
        reactions = False
        for lowercase, uppercase in zip(set(x.lower() for x in polymer), set(x.upper() for x in polymer)):
            while polymer.find(lowercase + uppercase) != -1:
                value1 = polymer.find(lowercase + uppercase)
                polymer = polymer[:value1] + polymer[value1 + 2:]
                reactions = True

            while polymer.find(uppercase + lowercase) != -1:
                value2 = polymer.find(uppercase + lowercase)
                polymer = polymer[:value2] + polymer[value2 + 2:]
                reactions = True
    return polymer


# Original solution which earned the stars, however takes a number of seconds for part 2 and very inefficient.
# Greatly improved in other solution file

part1 = react(original_polymer)
print "Part 1: Length after all reactions %d" % len(part1)

part2 = min(((len(react(part1.replace(letter, '').replace(letter.upper(), ''))), letter)
             for letter in set(letter.lower() for letter in part1)), key=lambda x: x[0])
print "Part 2: Minimum length is %d after removing %s/%s" % (part2[0], part2[1].upper(), part2[1])
