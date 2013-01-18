Kivy Profiler
===============

This is a thin wrapper of the memory_profiler and cProfile modules for python, designed to allow Kivy programmers and designers to make use of these profiling tools with very little additional work.

Memory Profiler
----------------

Keeps a line-by-line tally of which parts of your code increase the memory footprint of your app and the number of times these lines are called. To install, run `./install_memory_profiler.sh`. Requires pip.

Once memory_profiler is installed, use it by running the script `run_memory_profiler.sh`. The usage of this script is `run_memory_profiler.sh PYTHON_FILENAME LOGFILENAME`. For example, if you wanted to profile `../apps/AwesomeApp/main.py` and create the logfile `log.txt`, you could run `./run_memory_profiler.sh ../apps/AwesomeApp/main.py log.txt`.
