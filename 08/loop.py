import sys
import re

regex = r"(jmp|nop|acc) ([+-]\d+)"

instructions = []
for line in sys.stdin:
    parsed = re.match(regex, line.strip())
    instr = parsed.group(1)
    amount = int(parsed.group(2))
    instructions.append((instr, amount))

seen = [False for _ in range(len(instructions))]
acc = 0
instruction_pointer = 0
while not seen[instruction_pointer]:
    seen[instruction_pointer] = True
    (instr, amount) = instructions[instruction_pointer]
    if instr == "nop":
        instruction_pointer += 1
    elif instr == "acc":
        instruction_pointer += 1
        acc += amount
    else:  # jmp
        instruction_pointer += amount

print(acc)
