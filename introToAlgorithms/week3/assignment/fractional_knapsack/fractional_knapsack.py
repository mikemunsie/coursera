# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    knapsackValue = float(0)
    ratios = []

    # Sort item by the most valuable per quantity
    for index, value in enumerate(values):
      if index >= len(weights):
        break;
      ratios.append((float(weights[index])/float(value), float(value), float(weights[index])))

    # If no ratios have been created, break early
    if len(ratios) == 0:
      return 0

    ratios.sort(key=lambda tup: tup[0])

    # Continue picking items until our capacity has been met
    while len(ratios) > 0:

      # If the entire item fits, use it
      if capacity - ratios[0][2] > 0:
        capacity-= ratios[0][2]
        knapsackValue+= ratios[0][1]
        ratios.pop(0)

      # Otherwise take as much as we can from it (we can also short circuit)
      else:
        knapsackValue+= (capacity / ratios[0][2]) * ratios[0][1]
        break

    return knapsackValue


if __name__ == "__main__":
    '''
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    '''
    opt_value = get_optimal_value(50, [10,20], [20, 30])
    print("{:.10f}".format(opt_value))
