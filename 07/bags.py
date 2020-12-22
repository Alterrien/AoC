import re
import sys
from pprint import pprint


regex = r"(.*) bags contain ((no other bags)|(\d .*))."
bag_regex = r"^\d (.*) bag(s)?$"

contained = {}
for line in sys.stdin:
    parsed = re.match(regex, line)
    container = parsed.group(1)
    if parsed.group(3) is None:
        contained_bags = parsed.group(4).split(", ")
        for bag in contained_bags:
            contained_bag = re.match(bag_regex, bag).group(1)
            if contained_bag in contained:
                contained[contained_bag].add(container)
            else:
                contained[contained_bag] = {container}

in_gold_path = {bag for bag in contained["shiny gold"]}
to_process = [bag for bag in contained["shiny gold"]]
pprint(to_process)

while to_process and (bag := to_process.pop()):
    print(f"bag: {bag}")
    if bag in contained:
        for new_bag in contained[bag]:
            pprint(f"new bag: {new_bag}")
            if new_bag not in in_gold_path:
                in_gold_path.add(new_bag)
                pprint("gold path state")
                pprint(in_gold_path)
                to_process.append(new_bag)

print(len(in_gold_path))
