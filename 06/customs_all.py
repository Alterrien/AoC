import sys

acc = 0
answers = set("abcdefghijklmnopqrstuvwxyz")
for line in sys.stdin:
    if line.strip() == "":
        acc += len(answers)
        answers = set("abcdefghijklmnopqrstuvwxyz")
    else:
        answers = answers.intersection(line.strip())
else:
    acc += len(answers)

print(acc)
