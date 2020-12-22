import sys
from collections import Counter

valid_count = 0
for line in sys.stdin:
    (count, letter, pw) = line.split()
    (low_bound, high_bound) = count.split('-')
    low_bound = int(low_bound)
    high_bound = int(high_bound)
    letter = letter[0]
    counter = Counter(pw)
    if letter in counter and low_bound <= counter[letter] <= high_bound:
        valid_count += 1

print(valid_count)
