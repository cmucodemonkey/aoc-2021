input_list = open("Input\day2.txt", "r").read().split("\n")
x_change = 0
y_change = 0
aim = 0

for i in range(0, len(input_list)):
    temp = input_list[i].split(" ");

    if temp[0] == "forward":
        x_change += int(temp[1])
        y_change += (aim * int(temp[1]))
    elif temp[0] == "up":
        aim -= int(temp[1])
    elif temp[0] == "down":
        aim += int(temp[1])

print(x_change * y_change)
