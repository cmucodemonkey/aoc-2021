from collections import Counter

input_list = open("Input\day5.txt", "r").read().split("\n")
coordinate_list = []
count = 0

for item in input_list:
    firstPoint, secondPoint = item.split(" -> ")
    x1, y1 = map(int, firstPoint.split(","))
    x2, y2 = map(int, secondPoint.split(","))

    if x1 == x2 and y1 != y2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            coordinate_list.append((x1, y))
    elif x1 != x2 and y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            coordinate_list.append((x, y1))

elements_count = Counter(coordinate_list)
for key, value in elements_count.items():
    if value > 1:
        count += 1

print(count)