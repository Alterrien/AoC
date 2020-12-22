import sys

valid_count = 0
for line in sys.stdin:
    (count, letter, pw) = line.split()
    (low_bound, high_bound) = count.split('-')
    first_index = int(low_bound)
    second_index = int(high_bound)
    letter = letter[0]
    if (pw[first_index - 1] == letter) ^ (pw[second_index - 1] == letter):
        valid_count += 1

print(valid_count)
