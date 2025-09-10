def multimakedesign(design, towels):
    designs = len(design)
    TF = [0] * (designs + 1)
    TF[0] = 1  

    for i in range(1, designs + 1):
        for towel in towels:
            if i >= len(towel) and design[i - len(towel):i] == towel:
                TF[i] += TF[i - len(towel)]
    return TF[designs]

with open("dataaoc19.txt", "r") as f:
    lines = f.read().splitlines()

towel_patterns = lines[0].split(", ")
req_designs = lines[2:]

count = 0
for design in req_designs:
    count += multimakedesign(design,towel_patterns)

print(count)
