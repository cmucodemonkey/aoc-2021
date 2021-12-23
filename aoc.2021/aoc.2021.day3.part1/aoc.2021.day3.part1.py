input_list = open("Input.txt", "r").read().split("\n")
gamma_rate = ""
epsilon_rate = ""

for column in range(0, len(input_list[0])):
    zero_count = 0
    one_count = 0

    for row in range(0, len(input_list)):
        item = input_list[row]

        if item[column] == "0":
            zero_count += 1
        elif item[column] == "1":
            one_count += 1

    if zero_count > one_count:
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"

print(int(gamma_rate, 2) * int(epsilon_rate, 2))