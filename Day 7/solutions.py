import os

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
rules = {}

with open(input_path) as file:
    for line in file.readlines():
        before = line.split()[1]
        after = line.split()[7]

        if before not in rules:
            rules[before] = set()
        if after not in rules:
            rules[after] = set()
        rules[after].add(before)

done = []
tasks = sorted(rules.items(), key=lambda t: t[0])

while len(done) != len(tasks):
    for rule in tasks:
        if rule[0] not in done and all(x in done for x in rule[1]):
            done.append(rule[0])
            break

print "Part 1: %s" % ''.join(done)
