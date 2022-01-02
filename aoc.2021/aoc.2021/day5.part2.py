def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1)/(x2 - x1)

from collections import Counter

input_list = open("Input\day5.txt", "r").read().split("\n")
coordinate_list = []
count = 0

for item in input_list:
    first_point, second_point = item.split(" -> ")
    x1, y1 = map(int, first_point.split(","))
    x2, y2 = map(int, second_point.split(","))

    if x1 == x2 and y1 != y2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            coordinate_list.append((x1, y))
    elif x1 != x2 and y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            coordinate_list.append((x, y1))
    elif x1 != x2 and y1 != y2 and abs(calculate_slope(x1, y1, x2, y2)) == 1:
        x_delta = 1 if x1 < x2 else -1
        y_delta = 1 if y1 < y2 else -1

        x = x1
        y = y1

        while x != x2 and y != y2:
            coordinate_list.append((x, y))
            x += x_delta
            y += y_delta

        coordinate_list.append((x2, y2))

elements_count = Counter(coordinate_list)
for key, value in elements_count.items():
    if value > 1:
        count += 1

print(count)
