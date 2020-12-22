import sys

REQUIRED_KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0
passport = set()
for line in sys.stdin:
    if line.strip() == "":
        print("empty line")
        print(f"passport state: {passport}")
        if all(key in passport for key in REQUIRED_KEYS):
            print("valid passport")
            valid += 1
        passport = set()  # reset passport
    else:
        print(f"non-empty line: {line}")
        for kv in line.strip().split():
            passport.add(kv.split(":")[0])
else:
    print("empty line")
    print(f"passport state: {passport}")
    if all(key in passport for key in REQUIRED_KEYS):
        print("valid passport")
        valid += 1


print(valid)
