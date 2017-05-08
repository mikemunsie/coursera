# Uses python3
import sys
sys.setrecursionlimit(15000)

# Create a dict for lookup on already known sequence values
f = {}

def calc_fib(n):
  if (f.get(n)): return f.get(n)
  if (n <= 1): return n
  f[n] = calc_fib(n - 1) + calc_fib(n - 2)
  return f.get(n) % 10

n = int(input())
print(calc_fib(n))
