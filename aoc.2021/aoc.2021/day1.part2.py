input_list = open("Input\day1.txt", "r").read().split("\n")
count = 0

for i in range(0, len(input_list) - 3):
    sum1 = int(input_list[i]) + int(input_list[i + 1]) + int(input_list[i + 2])
    sum2 = int(input_list[i + 1]) + int(input_list[i + 2]) + int(input_list[i + 3])

    if sum2 > sum1:
        count += 1

print(count)

