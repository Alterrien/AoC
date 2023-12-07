from pprint import pprint

def stream_input(path):
    data = []
    with open(path) as f:
        for line in f:
            yield line.strip()

def is_digit(c):
    o = ord(c)
    return o >= 48 and o <= 57

class RangeMap():
    def __init__(self):
        self.ranges = []
        self.name = ''

    def add_range(self, line):
        data = line.split()
        dest = int(data[0])
        source = int(data[1])
        length = int(data[2])
        self.ranges.append({'source': source, 'length': length, 'dest': dest})

    def set_name(self, name):
        self.name = name

    def finalize(self):
        self.ranges.sort(key = lambda x: x['source'])

    def __repr__(self) -> str:
        return(f'RangeMap {self.name}')


    def get_dest_id(self, source_id):
        previous_range = None
        for r in self.ranges:
            if r['source'] > source_id:
                break
            else:
                previous_range = r

        if previous_range is None:
            return source_id
        elif source_id > previous_range['source'] + previous_range['length']:
            return source_id
        else:
            offset_to_source = source_id - previous_range['source']
            return previous_range['dest'] + offset_to_source

    def transform_range(self, source_id, length):
        all_ranges = []
        current_start = source_id
        remaining_length = length
        for r in self.ranges:
            if r['source'] + r['length'] < current_start:
                pass
            else:
                segment_length = 0
                # No segment
                if current_start < r['source']:
                    segment_length = r['source'] - current_start
                    source_range_end = r['source']
                    if (source_range_end - current_start) >= remaining_length:
                        segment_length = remaining_length
                        all_ranges.append((current_start, segment_length)) # no transform
                        break
                    else:
                        all_ranges.append((current_start, segment_length)) # no transform
                        current_start = r['source']
                        remaining_length = remaining_length - segment_length

                # In a Segment
                source_range_end = r['source'] + r['length']
                if (source_range_end - current_start) >= remaining_length:
                    segment_length = remaining_length
                    offset_to_source = current_start - r['source']
                    all_ranges.append((r['dest'] + offset_to_source, segment_length)) # To transform
                    break
                else:
                    offset_to_source = current_start - r['source']
                    segment_length = source_range_end - current_start
                    remaining_length = remaining_length - segment_length
                    all_ranges.append((r['dest'] + offset_to_source, segment_length)) # To transform
                    current_start += segment_length
        else:
            all_ranges.append((current_start, remaining_length))

        return self._merge_ranges(all_ranges)

    def _merge_ranges(_, ranges):
        ranges.sort(key = lambda x: x[0])
        merged = []
        running_start = ranges[0][0]
        running_length = ranges[0][1]
        previous_end =  running_start + running_length
        for r in ranges[1:]:
            (start, length) = r
            if previous_end == start:
                running_length += length
                previous_end = start + length
            else:
                merged.append((running_start, running_length))
                running_start = start
                running_length = length
        else:
            merged.append((running_start, running_length))

        return merged



def easy():
    input_gen = stream_input('2023/05/input')
    seeds_input = next(input_gen)
    seed_ids = seeds_input.split(':')[1].split()
    next(input_gen) # skip empty line
    all_range_maps = []
    curr_range_map = RangeMap()
    for line in input_gen:
        if line == '':
            curr_range_map.finalize()
            all_range_maps.append(curr_range_map)
            curr_range_map = RangeMap()
        elif is_digit(line[0]):
            curr_range_map.add_range(line)
        else:
            curr_range_map.set_name(line)

    else:
        curr_range_map.finalize()
        all_range_maps.append(curr_range_map)
        curr_range_map = None

    # pprint(all_range_maps)
    min_seed_id = 9999999999999999999999999999999
    for seed_id in seed_ids:
        current_id = int(seed_id)
        print(f'For seed id {seed_id}')
        for range_map in all_range_maps:
            current_id = range_map.get_dest_id(current_id)
            print(f'{range_map.name}: {current_id}')
        min_seed_id = min(min_seed_id, current_id)
        print('=================')

    print(min_seed_id)

def hard():
    input_gen = stream_input('2023/05/input')
    seeds_input = next(input_gen)
    seed_ids = seeds_input.split(':')[1].split()
    seed_ranges = []
    for i in range(0, len(seed_ids), 2):
        seed_ranges.append((int(seed_ids[i]), int(seed_ids[i+1])))

    next(input_gen) # skip empty line
    all_range_maps = []
    curr_range_map = RangeMap()
    for line in input_gen:
        if line == '':
            curr_range_map.finalize()
            all_range_maps.append(curr_range_map)
            curr_range_map = RangeMap()
        elif is_digit(line[0]):
            curr_range_map.add_range(line)
        else:
            curr_range_map.set_name(line)

    else:
        curr_range_map.finalize()
        all_range_maps.append(curr_range_map)
        curr_range_map = None

    min_location = 99999999999999999999999999999
    for seed_range in seed_ranges:
        print(f'======================for seed range {seed_range}')
        current_ranges = [seed_range]
        for range_map in all_range_maps:
            transformed_ranges = []
            for current_range in current_ranges:
                transformed_ranges = transformed_ranges + range_map.transform_range(current_range[0], current_range[1])
            current_ranges = range_map._merge_ranges(transformed_ranges)
            print(f'{range_map.name}: {current_ranges}')
        for e in transformed_ranges:
            min_location = min(min_location, e[0])
    print(min_location)

if __name__ == '__main__':
    # easy()
    hard()




    # # for i in range(100):
    # #     print(f'{i}, {seed_to_soil.get_dest_id(i)}')

    # # print(seed_to_soil.get_dest_id(50))
    # print(f'79, {seed_to_soil.get_dest_id(79)}')
    # print(f'14, {seed_to_soil.get_dest_id(14)}')
    # print(f'55, {seed_to_soil.get_dest_id(55)}')
    # print(f'13, {seed_to_soil.get_dest_id(13)}')
