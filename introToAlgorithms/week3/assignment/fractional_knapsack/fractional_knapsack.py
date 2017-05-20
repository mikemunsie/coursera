# Uses python3
import sys

# I've attempted this assignment multiple times and still get an out of bounds issue...
# This shouldn't be happening from what I can tell... moving on to a different problem.

def get_optimal_value(capacity, weights, values):
    knapsackValue = float(0)
    ratios = []

    # Sort item by the most valuable per quantity
    for index, value in enumerate(values):
      ratios.append((1.0 * weights[index]/values[index], weights[index], values[index]))
    ratios.sort(key=lambda x: x[0])

    # Continue picking items until our capacity has been met
    for ratio in ratios:
      amount = min(ratio[1], capacity)
      capacity-=amount
      knapsackValue+= 1.0 * amount / ratio[1] * ratio[2]
      if (capacity <= 0): break

    return knapsackValue


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    #opt_value = get_optimal_value(50, [20,50,30], [60, 100, 120])
    print("{:.10f}".format(opt_value))
