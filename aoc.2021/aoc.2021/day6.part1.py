fish_list = open("Input\day6.txt", "r").read().split(",")
days = 80

for day in range(days):
    zero_count = fish_list.count(0)
    fish_list = list(map(lambda value : 6 if value == 0 else int(value) - 1, fish_list))
    fish_list += [8] * zero_count

print(len(fish_list))