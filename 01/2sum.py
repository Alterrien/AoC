import sys

TARGET = 2020

if __name__ == '__main__':
    s = {int(line.strip()) for line in sys.stdin}
    for candidate in s:
        comp = 2020 - candidate
        if comp in s:
            print("FOUND")
            print(f"We have {candidate} and {comp}")
            print(f"Result is {candidate * comp}")
            break
    else:
        print("Found nothing")
