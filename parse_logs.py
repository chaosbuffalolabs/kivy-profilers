import sys
import re
from collections import defaultdict

check_re = re.compile(r'^ *([0-9]+) *([0-9\.]+) MB *([0-9\.]+) MB * (.*)$')
goodlines = []

with open(sys.argv[1],'r') as inf:
    for line in inf:
        r = check_re.match(line)
        if r is not None and r.group(3) != "0.00":
            goodlines.append([r.group(x) for x in range(1,5)])

linetracker = defaultdict(list)

for g in goodlines:
    linetracker[int(g[0])].append((float(g[1]),float(g[2])))

sorted_keys = sorted(linetracker.keys(), key=lambda x: -sum(y[1] for y in linetracker[x]))

for k in sorted_keys:
    print "Line %i: Total increase %f MB over %i calls." % (k, sum(y[1] for y in linetracker[k]), len(linetracker[k]))