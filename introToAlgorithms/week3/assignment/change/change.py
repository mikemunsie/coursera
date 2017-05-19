# Uses python3
import sys
import math

def get_change(m):
  counter = 0
  total = m
  if total >= 10:
    counter+=math.floor(total/10)
    total%=10
  if total >= 5:
    counter+=math.floor(total/5)
    total%=5
  counter+=total
  return int(counter)

if __name__ == '__main__':
  m = int(sys.stdin.read())
  print(get_change(m))
