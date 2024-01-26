'''
Statistical profiling
    - only collect metrics once in a while
    - snapshot of the running program's state at specified intervals
    - records a sample of the entire call stack
    - less overhead than deterministic. This overhead produces a lot of noise in the report

Pyinstrument
    - statistical profiler
    - can't handle multiple threads
    - or call functions implemented in C
'''

# monte carlo simulation for predicting the next value of pi
from random import uniform, random

def estimate_pi(n):
    return 4 * sum(hits(point()) for _ in range(n)) / n

def hits(point):
    return abs(point) <= 1

def point():
    # return complex(uniform(0, 1), uniform(0, 1))
    return complex(random(), random())

for exponent in range(1, 8):
    n = 10 ** exponent
    estimates = [estimate_pi(n) for _ in range(5)]
    print(f"{n = :<10,} {estimates}")

from pyinstrument import Profiler
# snapshot every 0.1 seconds, which might be low
# more frequent interval means higher overhead
with Profiler(interval=0.1) as profiler:
    # estimate pi with 10 million iterations
    estimate_pi(n=10_000_000)

profiler.print()
profiler.open_in_browser()