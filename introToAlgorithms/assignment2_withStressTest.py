# Uses python3
import random

# The faster routine (hopefully)
def getMaxPairwiseFast(numbers):
  newNumbers = list(numbers)
  def getMax(arr):
    maxN = 0
    popIndex = -1
    for i in range(0, len(arr)):
      if (arr[i] > maxN):
        maxN = arr[i]
        popIndex = i
    if (popIndex > -1):
      arr.pop(popIndex)
    return maxN
  maxn1 = getMax(newNumbers)
  maxn2 = getMax(newNumbers)
  print("MaxN1: ", maxn1)
  print("MaxN2: ", maxn2)
  return maxn1*maxn2

# Use this one to show an incorrect solution
def getMaxPairwiseFast_wrong(numbers):
  newNumbers = list(numbers)
  def getMax(arr):
    maxN = 0
    popIndex = -1
    for i in range(0, len(arr)):
      if (arr[i] > maxN):
        maxN = arr[i]
    return maxN
  maxn1 = getMax(newNumbers)
  maxn2 = getMax(newNumbers)
  return maxn1*maxn2

# The ol' slow routine
def getMaxPairwiseSlow(numbers):
  result = 0;
  for i in range(0, n):
    for j in range(i+1, n):
      if a[i]*a[j] > result:
        result = a[i]*a[j]
  return result

while(True):
  n = random.randint(2, 1000)
  a = []
  for i in range(0, n):
    a.append(random.randint(0, 100000))
  print(a)
  res1 = getMaxPairwiseSlow(a)
  res2 = getMaxPairwiseFast(a)
  if (res1 != res2):
    print("Wrong answer:", res1, " ", res2)
    break
  else:
    print('Ok')
  print("")




print(getMaxPairwiseFast(a))

# old way (not needed)
'''

'''
