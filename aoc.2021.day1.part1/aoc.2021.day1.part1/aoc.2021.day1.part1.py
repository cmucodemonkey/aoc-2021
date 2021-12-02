input_list = open("Input.txt", "r").read().split("\n")
count = 0

for i in range(0, len(input_list) - 1):
    if int(input_list[i]) < int(input_list[i + 1]):
        count += 1

print(count)