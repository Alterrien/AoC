from math import floor
from pprint import pprint

def stream_input(path):
    data = []
    with open(path) as f:
        for line in f:
            yield line.strip()


def parse_line(line):
    card_and_numbers = line.split(':')[1]
    split_numbers = card_and_numbers.split('|')
    winning = set(split_numbers[0].split())
    have = set(split_numbers[1].split())
    return (winning, have)

def get_input(path):
    data = []
    with open(path) as f:
        for line in f:
            winning, have = parse_line(line)
            data.append({'count': 1, 'points': len(winning & have)})

    return data

def hard():
    data = get_input('2023/04/input')
    for i, card in enumerate(data):
        print(f'==============Card {i}')
        pprint(data)
        nb_points = card['points']
        nb_cards = card['count']
        for j in range(i + 1, i + nb_points + 1):
            if j >= len(data):
                raise Exception('Out of Bounds')
            data[j]['count'] += (nb_cards)

    pprint(data)
    sum_cards = 0
    for card in data:
        sum_cards += card['count']

    print(sum_cards)


def easy():
    sum_points = 0
    for line in stream_input('2023/04/input'):
        print(line)
        w, h = parse_line(line)
        size = len(w & h)
        value = floor(2 ** (size - 1))
        print(f'size: {size}, value: {value}')
        sum_points += value


    print(sum_points)


if __name__ == '__main__':
    # easy()
    hard()