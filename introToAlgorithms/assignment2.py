# Uses python3

# My custom getMax routine (mutates, but hey I'm a noob at this python stuffs)
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

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)
maxn1 = getMax(a)
maxn2 = getMax(a)
result = maxn1*maxn2
print(result)

# old way (not needed)
'''
for i in range(0, n):
    for j in range(i+1, n):
        if a[i]*a[j] > result:
            result = a[i]*a[j]
'''
