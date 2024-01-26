'''
 - Perf is only available in linux as it is part of the OS kernel
 - Provides detailed information about the entire stack, including hardware events, system calls, library code, and more. Additionally, its overhead is small and adjustable.
'''

'''
Commands
 - sudo perf record -F 999 -o perf.data python 5-perf.py (creation of perf report)
 - sudo pert report (viewing of perf report)
 - sudo perf report --hierarchy --sort comm,dso,sample (summary or a more digestable view of the perf report)
'''

from concurrent.futures import ThreadPoolExecutor

def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def slow_function():
    print("Slow thread started")
    try:
        return find_divisors(100_000_000)
    finally:
        print("Slow thread ended")

def fast_function():
    print("Fast thread started")
    try:
        return find_divisors(50_000_000)
    finally:
        print("Fast thread ended")

def main():
    with ThreadPoolExecutor(max_workers=2) as pool:
        pool.submit(slow_function)
        pool.submit(fast_function)

    print("Main thread ended")

if __name__ == "__main__":
    main()