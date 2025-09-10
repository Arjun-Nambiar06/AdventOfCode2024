with open("dataaoc10.txt",'r') as f:
    lines = [line.strip() for line in f.readlines()]

start = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '0':
            start.append((i,j))
print(len(start))

count = 0
for pos in start:
    i,j = pos[0],pos[1]
    curr = 0
    valid = []
    visited = set((i,j))
    while True:
        if i < len(lines)-1 and int(lines[i+1][j]) == curr + 1 and (i + 1, j) not in visited:
            valid.append((i+1,j))
            visited.add((i+1,j))
        if i > 0 and int(lines[i-1][j]) == curr + 1 and (i - 1, j) not in visited:
            valid.append((i-1,j))
            visited.add((i-1,j))
        if j < len(lines[i])-1 and int(lines[i][j+1]) == curr + 1 and (i, j + 1) not in visited:
            valid.append((i,j+1))
            visited.add((i,j+1))
        if j > 0 and int(lines[i][j-1]) == curr + 1 and (i, j - 1) not in visited:
            valid.append((i,j-1))
            visited.add((i,j-1))
        if curr == 9:
            count += 1
        if valid == []:
            break
        new_start = valid.pop()
        i,j = new_start[0],new_start[1]
        curr = int(lines[i][j])
print(count)
        