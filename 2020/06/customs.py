import sys

acc = 0
answers = set()
for line in sys.stdin:
    if line.strip() == "":
        acc += len(answers)
        answers = set()
    else:
        answers = answers.union(line.strip())
else:
    acc += len(answers)

print(acc)
