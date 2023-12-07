from math import sqrt, ceil, floor

def get_input(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(line)

    return data

def roots(t, d):
    delta = (t ** 2) - (4 * d)
    x_1 = (-t + sqrt(delta)) / -2
    x_2 = (-t - sqrt(delta)) / -2
    print(f'actual roots: {x_1}, {x_2}')
    # ceil of second root to put neately inside of range
    # floor + 1 of first one to deal with integer roots
    if x_1 > x_2:
        return (floor(x_2 + 1), ceil(x_1))
    else:
        return (floor(x_1 + 1), ceil(x_2))

def easy():
    data = get_input('2023/06/input')
    times = [int(x) for x in data[0].split(':')[1].split()]
    distances = [int(x) for x in data[1].split(':')[1].split()]
    acc = 1
    for (t, d) in zip(times, distances):
        print(f't {t}, d {d}')
        low, high = roots(t, d)
        print(f'low {low}, high {high}')
        # print(len(range(low, high)))
        acc *= low - high
    print(acc)

def hard():
    data = get_input('2023/06/input')
    time = int(''.join(data[0].split(':')[1].split()))
    distance = int(''.join(data[1].split(':')[1].split()))
    low, high = roots(time, distance)
    print(high - low)


if __name__ == '__main__':
    easy()
    hard()