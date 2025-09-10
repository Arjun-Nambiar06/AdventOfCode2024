import csv

def is_valid_case(case, rules):
    for prev, next in rules:
        if prev in case and next in case:
            if case.index(prev) > case.index(next):
                return False
    return True

def sort(case,rules):
    sorted=[]
    for i in range(len(case)):
        sorted.append(case[i])
        srtd = False
        for j in range(i):
            if case[i]!=sorted[j]:
                for k in rules:
                    if srtd == False and k[0]==case[i] and k[1]==sorted[j]:
                        sorted.remove(case[i])
                        sorted.insert(j,case[i])
                        srtd = True  
    return sorted

with open("values1_aoc5.csv", "r") as f:
    reader = csv.reader(f)
    rules = [tuple(int(i) for i in row) for row in reader]

with open("values2_aoc5.csv", "r") as f:
    reader = csv.reader(f)
    cases = [[int(i.strip()) for i in row if i.strip().isdigit()] for row in reader]

middle_sum = 0
for case in cases:
    if is_valid_case(case, rules)==False:
        case = sort(case,rules)
        middle_sum += case[len(case)//2]
print(middle_sum)
