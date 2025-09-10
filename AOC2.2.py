import csv

def is_safe(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

filename = "valuesaoc2.csv"
total_safe = 0

with open("valuesaoc2.csv", 'r') as f:
    rdr = csv.reader(f)
    for list in rdr:
        report=[]
        for i in list:
            if i != '':
                report.append(int(i))
            
        if is_safe(report):
            total_safe += 1
            continue

        for i in range(len(report)):
            new_rep = report[:i] + report[i+1:]
            if is_safe(new_rep):
                total_safe += 1
                break
print(f"Total Safe Reports (with Dampener): {total_safe}")
