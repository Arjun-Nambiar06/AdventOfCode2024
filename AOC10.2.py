with open("dataaoc10.txt", 'r') as f:
    lines = [line.strip() for line in f.readlines()]

start = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '0':
            start.append((i, j))
print(len(start))

total_rating = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
for pos in start:
    i, j = pos[0], pos[1]
    valid = [(i, j, 0)]  
    trail_count = 0

    while valid:
        x, y, curr_value = valid.pop()

       
        if int(lines[x][y]) == 9:
            trail_count += 1
            continue

       
        for changex, changey in directions:
            newx, newy = x + changex, y + changey
            if 0 <= newx < len(lines) and 0 <= newy < len(lines[0]):
                if int(lines[newx][newy]) == curr_value + 1:  
                    valid.append((newx, newy, curr_value + 1))

    total_rating += trail_count  

print(total_rating)
