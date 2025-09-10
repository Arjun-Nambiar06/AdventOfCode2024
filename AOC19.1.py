def makedesign(design, towels):
    designs = len(design)
    TF = [False] * (designs + 1)
    TF[0] = True  

    for i in range(1, designs + 1):
        for towel in towels:
            if i >= len(towel) and design[i - len(towel):i] == towel:
                TF[i] = TF[i] or TF[i - len(towel)]
    return TF[designs]

with open("dataaoc19.txt", "r") as f:
    lines = f.read().splitlines()

towel_patterns = lines[0].split(", ")
req_designs = lines[2:]

count = 0
for design in req_designs:
    if makedesign(design, towel_patterns):
        count += 1

print(count)
