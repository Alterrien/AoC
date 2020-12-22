import re
import sys
from pprint import pprint

regex = r"(.*) bags contain ((no other bags)|(\d .*))."
bag_regex = r"^(\d) (.*) bag(s)?$"


contain = {}
for line in sys.stdin:
    parsed = re.match(regex, line)
    container = parsed.group(1)
    if parsed.group(3) is None:
        contained_bags = parsed.group(4).split(", ")
        for bag in contained_bags:
            contained_bag = re.match(bag_regex, bag)
            contained_bag_color = contained_bag.group(2)
            contained_bag_amount = contained_bag.group(1)
            if container in contain and contained_bag_color in contain[container]:
                print(f"Error: {contained_bag} already present")
                exit(1)
            elif container not in contain:
                contain[container] = {contained_bag_color: contained_bag_amount}
            else:
                contain[container][contained_bag_color] = contained_bag_amount

to_process = [
    (bag_color, int(contain["shiny gold"][bag_color]))
    for bag_color in contain["shiny gold"]
]
pprint(f"to process, {to_process}")
acc = 0
while to_process and (bag := to_process.pop()):
    pprint(f"Currently processing: {bag}")
    (color, amount) = bag
    acc += amount
    if color not in contain:
        print(f"Color {color} does contain other bags, it is held {amount} times")
    else:
        for newbag in contain[color]:
            new_amount = int(contain[color][newbag])
            print(
                f"adding {newbag}, contained {new_amount} times current acc: {amount}"
            )
            to_process.append((newbag, amount * new_amount))

pprint(to_process)

print(acc)