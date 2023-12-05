from pprint import pprint


ALL_DIGITS = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

def stream_input(path):
    data = []
    with open(path) as f:
        for line in f:
            yield line.strip()

def get_input(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(line)

    return data


def mark_and_append(grid, i, j, adjacent_numbers):
    if not (0 <= i < len(grid) and 0 <= j < len(grid[i])):
        return
    elmt = grid[i][j]
    if elmt is not None and 'data' in elmt and not elmt['data']['mark']:
        elmt['data']['mark'] = True
        print(f'{i}, {j} marked')
        adjacent_numbers.append(elmt['data']['value'])

def item_is_special_char(grid, i, j):
    # print(f'special char detection: {i}, {j}')
    if not (0 <= i < len(grid) and 0 <= j < len(grid[i])):
        return False
    else:
        # print(f'in bounds')
        elmt = grid[i][j]
        # print(elmt)
        if elmt in ALL_DIGITS or elmt == '.':
            return False
        else:
            # print('Found special char')
            return True


def resolve_number(number, grid, i, j):
    # print(f'Flush acc: {acc_number}')
    print(f'Number {number} starting to detect for special char')
    start_i = i - 1
    end_i = i + 2
    start_j = j - len(number) - 1
    end_j = j + 1
    found_special_char = False
    for sub_i in range (start_i, end_i):
        for sub_j in range(start_j, end_j):
            if item_is_special_char(grid, sub_i, sub_j):
                found_special_char = True
                # print(f'Found special char: {sub_i}, {sub_j}')
                break
        if found_special_char:
            break
    if found_special_char:
        return int(number)
    else:
        return 0
    # print(number_start_j)

def resolve_number_hard(number, grid, i, j):
    print(f'Marking for {number} in {i}, {j}')
    # Pointers go vroom
    data = {'value': int(number), 'mark': False}
    for k in range(j - 1, j - (len(number) + 1), -1):
        if grid[i][k] is not None:
            grid[i][k]['data'] = data


def easy():
    symbols_indexes = set()
    numbers = {}
    grid = []
    data = get_input('2023/03/input')
    sum_part_numbers = 0
    for i, line in enumerate(data):
        curr = []
        grid.append(curr)
        # print(line)
        acc_number = ''
        for j, c in enumerate(line.strip()):
            # print(c)
            if c in ALL_DIGITS:
                # print(f'acc: {c}')
                curr.append({'c': c})
                acc_number = f'{acc_number}{c}'
            else:
                if c != '.':
                    symbols_indexes.add((i, j))
                    curr.append({'c': c})
                else:
                    curr.append(None)

                if acc_number != '':
                    sum_part_numbers += resolve_number(acc_number, grid, i, j)
                    acc_number = ''
        else:
            if acc_number != '':
                sum_part_numbers += resolve_number(acc_number, grid, i, j)
                acc_number = ''

    # pprint(symbols_indexes)
    # pprint(numbers)
    # pprint(grid)

    print(sum_part_numbers)


def hard():
    stars_indexes = set()
    grid = []
    data = get_input('2023/03/input')
    sum_part_numbers = 0
    for i, line in enumerate(data):
        curr = []
        grid.append(curr)
        # print(line)
        acc_number = ''
        for j, c in enumerate(line.strip()):
            # print(c)
            if c in ALL_DIGITS:
                # print(f'acc: {c}')
                curr.append({'c': c})
                acc_number = f'{acc_number}{c}'
            else:
                if c == '*':
                    stars_indexes.add((i, j))
                    curr.append({'c': c})
                else:
                    curr.append(None)

                if acc_number != '':
                    resolve_number_hard(acc_number, grid, i, j)
                    acc_number = ''
        else:
            if acc_number != '':
                resolve_number_hard(acc_number, grid, i, j)
                acc_number = ''

    # pprint(symbols_indexes)
    # pprint(numbers)
    # pprint(grid)

    sum_gear_ratio = 0
    for (i, j) in stars_indexes:
        adjacent_numbers = []
        mark_and_append(grid, i - 1, j - 1, adjacent_numbers)
        mark_and_append(grid, i - 1, j    , adjacent_numbers)
        mark_and_append(grid, i - 1, j + 1, adjacent_numbers)
        mark_and_append(grid, i    , j - 1, adjacent_numbers)
        mark_and_append(grid, i    , j    , adjacent_numbers)
        mark_and_append(grid, i    , j + 1, adjacent_numbers)
        mark_and_append(grid, i + 1, j - 1, adjacent_numbers)
        mark_and_append(grid, i + 1, j    , adjacent_numbers)
        mark_and_append(grid, i + 1, j + 1, adjacent_numbers)
        if len(adjacent_numbers) == 2:
            sum_gear_ratio += (adjacent_numbers[0] * adjacent_numbers[1])

    print(sum_gear_ratio)




if __name__ == '__main__':
    # easy()
    hard()