# Uses python3

# Create a dict for lookup on already known sequence values
f = {}

def calc_fib(n):
  if (f.get(n)): return f.get(n)
  if (n <= 1): return n
  f[n] = calc_fib(n - 1) + calc_fib(n - 2)
  return f.get(n)

def fibonacci_sum(n):
    calc_fib(n)
    sum = 0
    for i in range(n + 1):
        sum+=(0 if f.get(i) is None else f.get(i))
    return sum % 10

n = int(input())
print(fibonacci_sum(n))
