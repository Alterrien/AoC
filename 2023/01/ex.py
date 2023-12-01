import re

def get_input(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(line)

    return data

def stream_input(path):
    data = []
    with open(path) as f:
        for line in f:
            yield line.strip()

def is_digit(c):
    o = ord(c)
    return o >= 49 and o <= 57


def easy():
    curr_sum = 0
    for line in stream_input('2023/01/input'):
        print(line)
        first = 0
        last = 0
        for c in line:
            if is_digit(c):
                first = int(c)
                break
        else:
            raise Exception('first digit not found')
        for c in line[::-1]:
            if is_digit(c):
                last = int(c)
                break
        else:
            raise Exception('last digit not found')
        curr_sum += first * 10 + last
    print(curr_sum)
def hard():
    REGEX = r'(twone|oneight|threeight|fiveight|nineight|sevenine|eightwo|one|two|three|four|five|six|seven|eight|nine|[0-9])'
    MATCHES = {
        'one': [1],
        'two': [2],
        'three': [3],
        'four': [4],
        'five': [5],
        'six': [6],
        'seven': [7],
        'eight': [8],
        'nine': [9],
        'twone': [2, 1],
        'oneight': [1, 8],
        'threeight': [3, 8],
        'fiveight': [5, 8],
        'nineight': [9, 8],
        'sevenine': [7, 9],
        'eightwo': [8, 2],
        '1': [1],
        '2': [2],
        '3': [3],
        '4': [4],
        '5': [5],
        '6': [6],
        '7': [7],
        '8': [8],
        '9': [9],
    }
    curr_sum = 0
    first = 0
    last = 0
    for line in stream_input('2023/01/input'):
        print(line)
        matches = re.findall(REGEX, line)
        print(matches)
        first = MATCHES[matches[0]][0]
        last = MATCHES[matches[-1]][-1]
        print(first * 10 + last)
        curr_sum += first * 10 + last
    print(curr_sum)


if __name__ == '__main__':
    # easy()
    hard()