import sys
import re

regex = r"(jmp|nop|acc) ([+-]\d+)"


def do_run(instructions):
    seen = [False for _ in range(len(instructions))]
    acc = 0
    instruction_pointer = 0
    while (instruction_pointer != len(instructions)) and (
        not seen[instruction_pointer]
    ):
        seen[instruction_pointer] = True
        (instr, amount) = instructions[instruction_pointer]
        if instr == "nop":
            instruction_pointer += 1
        elif instr == "acc":
            instruction_pointer += 1
            acc += amount
        else:  # jmp
            instruction_pointer += amount
    return (instruction_pointer == len(instructions), acc)


instructions = []
for line in sys.stdin:
    parsed = re.match(regex, line.strip())
    instr = parsed.group(1)
    amount = int(parsed.group(2))
    instructions.append((instr, amount))

seen = [False for _ in range(len(instructions))]
acc = 0
for i in range(len(instructions)):
    (instr, amount) = instructions[i]
    if instr == "nop":
        instructions[i] = ("jmp", amount)
        (finished, acc) = do_run(instructions)
        instructions[i] = ("nop", amount)
    elif instr == "jmp":
        instructions[i] = ("nop", amount)
        (finished, acc) = do_run(instructions)
        instructions[i] = ("jmp", amount)

    if finished:
        print(acc)
        break
else:
    print("Has not found permutation")