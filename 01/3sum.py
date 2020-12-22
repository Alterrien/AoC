import sys
from itertools import combinations

TARGET = 2020

if __name__ == "__main__":
    t = [int(line.strip()) for line in sys.stdin]
    s = set(t)
    for cand1, cand2 in combinations(t, 2):
        comp = 2020 - (cand1 + cand2)

        if comp > 0:
            print(f"{cand1} and {cand2} -> {comp}")

        if comp in s:
            print("FOUND")
            print(f"We have {cand1}, {cand2} and {comp}")
            print(f"Result is {cand1 * cand2 * comp}")
            break
    else:
        print("Found nothing")
