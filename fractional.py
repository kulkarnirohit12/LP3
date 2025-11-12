def fractional_knapsack(value, weight, capacity):
    ratio = [(v/w, v, w) for v, w in zip(value, weight)]
    ratio.sort(reverse=True)
    total_value = 0
    for r, v, w in ratio:
        if capacity >= w:
            capacity -= w
            total_value += v
        else:
            total_value += v * (capacity / w)
            break
    return total_value

values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
print("Maximum value:", fractional_knapsack(values, weights, W))
