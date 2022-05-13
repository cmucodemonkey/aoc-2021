from collections import defaultdict

fish_list = open("Input\day6.txt", "r").read().split(",")
days = 256
fish_map = {}

# Map each reproductive state to the number of fish in that state (i.e. {1, 50}, {2, 35}, etc.)
for fish in fish_list:
    if fish not in fish_map:
        fish_map[fish] = 0
    fish_map[fish] += 1

for day in range(days):
    updated_fish_map = defaultdict(int)

    for state, count in fish_map.items():
        if state == 0:
            # Reset the status of reproducing fish back to 6
            updated_fish_map[6] += count
            # Add the new baby fish
            updated_fish_map[8] += count
        else:
            # Decrement the status of all other fish
            updated_fish_map[int(state) - 1] += count

        fish_map = updated_fish_map

print(sum(fish_map.values()))