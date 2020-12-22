import sys
from itertools import count

first_line = input()
slide_length = len(first_line)
indexes1 = ((i * 1) % slide_length for i in count(1, 1))
indexes3 = ((i * 3) % slide_length for i in count(1, 1))
indexes5 = ((i * 5) % slide_length for i in count(1, 1))
indexes7 = ((i * 7) % slide_length for i in count(1, 1))
indexes2 = ((i * 0.5) % slide_length for i in count(1, 1))

count_og = 1 if first_line[0] == "#" else 0
counts = {
    "1": count_og,
    "3": count_og,
    "5": count_og,
    "7": count_og,
    "2": count_og,
}

flip = False

for (i1, i3, i5, i7, i2, line) in zip(
    indexes1, indexes3, indexes5, indexes7, indexes2, sys.stdin
):
    if line[i1] == "#":
        counts["1"] += 1
    if line[i3] == "#":
        counts["3"] += 1
    if line[i5] == "#":
        counts["5"] += 1
    if line[i7] == "#":
        counts["7"] += 1
    if flip:
        if line[int(i2)] == "#":
            counts["2"] += 1
        flip = False
    else:
        flip = True

print(counts["1"] * counts["3"] * counts["5"] * counts["7"] * counts["2"])
