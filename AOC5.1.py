import csv

def is_valid_case(case, rules):
    for prev, next in rules:
        if prev in case and next in case:
            if case.index(prev) > case.index(next):
                return False
    return True

with open("values1_aoc5.csv", "r") as f:
    reader = csv.reader(f)
    rules = [tuple(int(i) for i in row) for row in reader]

with open("values2_aoc5.csv", "r") as f:
    reader = csv.reader(f)
    cases = [[int(i.strip()) for i in row if i.strip().isdigit()] for row in reader]

middle_sum = 0
for case in cases:
    if is_valid_case(case, rules):
        middle_sum += case[len(case)//2]
print(middle_sum)
