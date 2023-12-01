import sys
import heapq

def easy():
    input_data = []
    acc = []
    for line in sys.stdin:
        if line.strip() == '':
            input_data.append(acc)
            acc = []
        else:
            acc.append(int(line.strip()))


    max_i = -1
    max_sum = 0
    for i, elf in enumerate(input_data):
        curr_sum = sum(elf)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_i = i

    print(f'The max index is {max_i} with calories {max_sum}')

def hard():
    h = []
    acc = 0
    for line in sys.stdin:
        if line.strip() == '':
            heapq.heappush(h, acc)
            acc = 0
        else:
            acc += int(line.strip())

    sum3 = sum(heapq.nlargest(3, h))
    print(f'The sum of 3 most loaded elves is {sum3}')

if __name__ == '__main__':
    # easy()
    hard()