import sys
import re
from collections import defaultdict
from plot import LinePlot, PlotExplorer
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout



check_re = re.compile(r'^ *([0-9]+) *([0-9\.]+) MB *([0-9\.]+) MB * (.*)$')
timestamp_re = re.compile(r'^TIMESTAMP: ([0-9\.]+)')

all_log_lines = []
increase_lines = []

start_timestamp = None
current_timestamp = 0
logged_current_timestamp = False

with open(sys.argv[1],'r') as inf:
    for line in inf:
        r = check_re.match(line)
        t = timestamp_re.match(line)
        if r is not None:
            if not logged_current_timestamp:
                all_log_lines.append([current_timestamp] + [r.group(x) for x in range(1,5)])    
                logged_current_timestamp = True
            try:
                if float(r.group(3)) != 0:
                    increase_lines.append([current_timestamp] + [r.group(x) for x in range(1,5)])
            except:
                continue
        if t is not None:
            if start_timestamp is None:
                start_timestamp = float(t.group(1))
                current_timestamp = 0
            else:
                current_timestamp = float(t.group(1)) - start_timestamp
            logged_current_timestamp = False


linetracker = defaultdict(list)
timetracker = defaultdict(list)
total_mem = [(x[0], float(x[2])) for x in all_log_lines]

for g in increase_lines:
    linetracker[int(g[1])].append((float(g[2]),float(g[3])))
    timetracker[g[0]].append(g[1:])

sorted_keys = sorted(linetracker.keys(), key=lambda x: -sum(y[1] for y in linetracker[x]))

annotations = {k: sorted(timetracker[k], key=lambda x: -float(x[2]))[:3] for k in timetracker.keys()}

for k in sorted_keys:
    print "Line %i: Total increase %f MB over %i calls." % (k, sum(y[1] for y in linetracker[k]), len(linetracker[k]))

Builder.load_file('plot.kv')

class ParseLogsApp(App):
    def build(self):
        lp = LinePlot(total_mem, line_width = 5., tick_distance_x=5, tick_distance_y=10)
        m = PlotExplorer(lp, annotations)
        return m

ParseLogsApp().run()