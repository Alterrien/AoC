import re

def stream_input(path):
    data = []
    with open(path) as f:
        for line in f:
            yield line.strip()


def easy():
    MAXES = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    R_GAME_ID = r'^Game (\d+)'
    R_SAMPLE = r'(\d+) (red|green|blue)'
    sum_ids = 0
    for line in stream_input('2023/02/input'):
        s = line.strip()
        print(line)
        game_id = re.match(R_GAME_ID, s).groups()[0]
        samples = re.findall(R_SAMPLE, s)
        print(game_id)
        print(samples)
        for sample in samples:
            (count, color) = sample
            if int(count) > MAXES[color]:
                print("impossible")
                break
        else:
            sum_ids += int(game_id)
    print(sum_ids)


def hard():
    R_SAMPLE = r'(\d+) (red|green|blue)'
    sum_power = 0
    for line in stream_input('2023/02/input'):
        maxes = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        samples = re.findall(R_SAMPLE, line.strip())
        for sample in samples:
            (count, color) = sample
            maxes[color] = max(int(count), maxes[color])
        sum_power += maxes['red'] * maxes['green'] * maxes['blue']
    print(sum_power)






if __name__ == '__main__':
    # easy()
    hard()