import sys


def compute_row(boarding_id):
    rows = boarding_id[:7]
    to_bin = ["0" if c == "F" else "1" for c in rows]
    return int("".join(to_bin), 2)


def compute_column(boarding_id):
    rows = boarding_id[7:]
    to_bin = ["0" if c == "L" else "1" for c in rows]
    return int("".join(to_bin), 2)


max_value = 0
all_ids = []
for line in sys.stdin:
    row = compute_row(line.strip())
    column = compute_column(line.strip())
    boarding_id = row * 8 + column
    max_value = max(max_value, boarding_id)
    all_ids.append(boarding_id)

all_ids.sort()
last = 44
for i in all_ids:
    if i != last + 1:
        print(last + 1)
        break
    else:
        last = i

print(max_value)
