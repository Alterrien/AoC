import sys
import re

REQUIRED_KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


class Checker:
    def __init__(self, p):
        self.p = p

    @property
    def valid_byr(self):
        if "byr" in self.p:
            byr = self.p["byr"]
            return byr.isdigit() and (1920 <= int(byr) <= 2002)
        else:
            return False

    @property
    def valid_iyr(self):
        if "iyr" in self.p:
            iyr = self.p["iyr"]
            return iyr.isdigit() and (2010 <= int(iyr) <= 2020)
        else:
            return False

    @property
    def valid_eyr(self):
        if "eyr" in self.p:
            eyr = self.p["eyr"]
            return eyr.isdigit() and (2020 <= int(eyr) <= 2030)
        else:
            return False

    @property
    def valid_hgt(self):
        regex = r"^(\d+)(in|cm)$"
        if "hgt" in self.p:
            res = re.match(regex, self.p["hgt"])
            if res:
                unit = res.group(2)
                size = int(res.group(1))
                if unit == "in":
                    return 59 <= size <= 76
                else:
                    return 150 <= size <= 193
            else:
                return False
        else:
            return False

    @property
    def valid_hcl(self):
        regex = r"^#[0-9a-f]{6}$"
        return "hcl" in self.p and bool(re.match(regex, self.p["hcl"]))

    @property
    def valid_ecl(self):
        regex = r"^(amb|brn|blu|gry|grn|hzl|oth)$"
        return "ecl" in self.p and bool(re.match(regex, self.p["ecl"]))

    @property
    def valid_pid(self):
        regex = r"[0-9]{9}"
        return "pid" in self.p and bool(re.match(regex, self.p["pid"]))

    @property
    def passport_valid(self):
        return (
            self.valid_byr
            and self.valid_iyr
            and self.valid_eyr
            and self.valid_hgt
            and self.valid_hcl
            and self.valid_ecl
            and self.valid_pid
        )


valid = 0
passport = {}
for line in sys.stdin:
    if line.strip() == "":
        print("empty line")
        print(f"passport state: {passport}")
        checker = Checker(passport)
        if checker.passport_valid:
            print("valid passport")
            valid += 1
        passport = {}  # reset passport
    else:
        print(f"non-empty line: {line}")
        for kv in line.strip().split():
            (key, value) = kv.split(":")
            passport[key] = value
else:
    print("empty line")
    print(f"passport state: {passport}")
    checker = Checker(passport)
    if checker.passport_valid:
        print("valid passport")
        valid += 1

print(valid)
