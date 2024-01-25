'''
- Also available in pure python profile but cProfile is preferred since it is more performant
- Deterministic Profiling
    - traces all function calls in your program
    - meant to reflect the fact that all function call, function return, and exception events are monitored, and precise timings are made for the intervals between these events (during which time the user’s code is executing). 
- Statistical Profiling - randomly samples the effective instruction pointer, and deduces where time is being spent. The latter technique traditionally involves less overhead (as the code does not need to be instrumented), but provides only relative indications of where time is being spent
'''

from cProfile import Profile
from pstats import SortKey, Stats

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)

with Profile() as profile:
    print(f"{fib(35) = }")
    (
        Stats(profile)
        .strip_dirs()
        .sort_stats(SortKey.CALLS)
        .print_stats()
    )

'''
- primitive means non-recursive calls
- pStats help format, sort, and print the collected runtime statistics
- most of the recursive calls are redundant because they keep calculating the same values (use memoization)
- profiling adds noticeable runtime overhead due to keeping track of certain events. This may be a problem in systems have already have poor performance

fib(35) = 9227465
         29860712 function calls (10 primitive calls) in 9.376 seconds

   Ordered by: call count

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
29860703/1    9.376    0.000    9.376    9.376 3-cProfile.py:12(fib)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 cProfile.py:51(create_stats)
        1    0.000    0.000    0.000    0.000 pstats.py:107(__init__)
        1    0.000    0.000    0.000    0.000 pstats.py:117(init)
        1    0.000    0.000    0.000    0.000 pstats.py:136(load_stats)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''