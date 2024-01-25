'''
- Can run once before profiling if one-time setup is required
- Best result -> closest truth while longer runs means disturbance from random noise
- Limitation is that it only measures execution time. Lacks more detailed metrics
'''

from timeit import timeit

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)

iterations = 100

# runs the fib function with a parameter of 30 a 100 times and gets its average runtime
# default number of iterations is 5
total_time = timeit("fib(30)", number=iterations, globals=globals())

print(f"Average time is {total_time / iterations:.2f} seconds")

'''
CLI version

SETUP_CODE="def fib(n): return n if n < 2 else fib(n - 2) + fib(n - 1)"
python3 -m timeit -s "$SETUP_CODE" -r 100 "fib(30)"
'''