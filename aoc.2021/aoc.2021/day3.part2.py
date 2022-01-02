file_name = "Input\day3.txt"
input_list = open(file_name, "r").read().split("\n")

for column in range(0, len(input_list[0])):
    zero_list = []
    one_list = []

    for row in range(0, len(input_list)):
        item = input_list[row]

        if item[column] == "0":
            zero_list.append(item)
        elif item[column] == "1":
            one_list.append(item)

    if len(input_list) == 1:
        break
    elif len(one_list) >= len(zero_list):
        input_list = one_list
    else:
        input_list = zero_list

oxygen_generator_rating = input_list[0]
input_list = open(file_name, "r").read().split("\n")

for column in range(0, len(input_list[0])):
    zero_list = []
    one_list = []

    for row in range(0, len(input_list)):
        item = input_list[row]

        if item[column] == "0":
            zero_list.append(item)
        elif item[column] == "1":
            one_list.append(item)

    if len(input_list) == 1:
        break
    elif len(zero_list) <= len(one_list):
        input_list = zero_list
    else:
        input_list = one_list

CO2_scrubber_rating = input_list[0]
print(int(oxygen_generator_rating, 2) * int(CO2_scrubber_rating, 2))