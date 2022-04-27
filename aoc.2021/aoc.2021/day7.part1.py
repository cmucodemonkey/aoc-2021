import numpy as np

input = sorted([16,1,2,0,4,2,7,1,2,14])
mid = np.percentile(input,[50])
fuel_cost = 0

for value in input:
    fuel_cost += abs(value - mid)

print(fuel_cost)
