import os
import re
from datetime import datetime, timedelta
from collections import defaultdict, Counter

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(input_path) as file:
    regex = re.compile(r'\[(?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2})]\s(?P<message>.+)')

    sorted_values = sorted(
        [(datetime.strptime(re.match(regex, line).group('timestamp'), '%Y-%m-%d %H:%M'),
          re.match(regex, line).group('message'))
         for line in
         file.readlines()], key=lambda x: x[0])

guard_id_regex = re.compile(r'Guard\s#(?P<guard_id>\d+)\sbegins\sshift')

asleep_dict = defaultdict(list)

current_guard = 0
current_asleep_time = 0

for line in sorted_values:
    if re.match(guard_id_regex, line[1]):
        current_guard = re.match(guard_id_regex, line[1]).group('guard_id')
    elif "falls asleep" in line:
        current_asleep_time = line[0]
    elif "wakes up" in line:
        mins = (line[0] - current_asleep_time).seconds / 60
        for time in (current_asleep_time + timedelta(minutes=x) for x in xrange(mins)):
            asleep_dict[current_guard].append(str(time.time().minute))

# Part 1
most_asleep_guard = max((len(v), k) for k, v in asleep_dict.iteritems())[1]
most_common_minute_asleep = Counter(asleep_dict[most_asleep_guard]).most_common(1)[0][0]

print "ID of guard who spent most time asleep: %s" % most_asleep_guard
print "Minute guard was most asleep: %s" % most_common_minute_asleep
print "Part 1 answer: %d" % (int(most_asleep_guard) * int(most_common_minute_asleep))

# Part 2
most_freq_tuple = max(((Counter(v).most_common(1)[0], k) for k, v in asleep_dict.iteritems()), key=lambda x: x[0][1])
print "Guard %s was most frequently asleep on minute %s (a total of %d times)" % (most_freq_tuple[1],
                                                                                  most_freq_tuple[0][0],
                                                                                  most_freq_tuple[0][1])
print "Part 2 answer: %d" % (int(most_freq_tuple[1]) * int(most_freq_tuple[0][0]))
