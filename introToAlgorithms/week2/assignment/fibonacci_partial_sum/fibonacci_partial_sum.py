# Uses python3
import sys

# Create a dict for lookup on already known sequence values
f = {}

def calc_fib(n):
  if (f.get(n)): return f.get(n)
  if (n <= 1): return n
  f[n] = calc_fib(n - 1) + calc_fib(n - 2)
  return f.get(n)

def fibonacci_partial_sum_naive(from_, to):
    calc_fib(to)
    sum = 0
    for i in range(to + 1):
        if i >= from_:
            sum+=(0 if f.get(i) is None else f.get(i))
    return sum % 10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))