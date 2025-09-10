def looping(lines,row,col,direction):
    visited = set()
    while 0 <= row < len(lines) and 0 <= col < len(lines[0]):
        if (row,col,direction) in visited:
            return True
        visited.add((row,col,direction))

        if direction == '^' and ((row > 0 and lines[row - 1][col] != '#') or row == 0):
            row -= 1
        elif direction == '>' and ((col < len(lines[0]) - 1 and lines[row][col + 1] != '#') or col == len(lines[0])-1):
            col += 1
        elif direction == 'v' and ((row < len(lines) - 1 and lines[row + 1][col] != '#') or row == len(lines)-1):
            row += 1
        elif direction == '<' and ((col > 0 and lines[row][col - 1] != '#') or col == 0):
            col -= 1
        else:
            direction = {'^': '>', '>': 'v', 'v': '<', '<': '^'}[direction]

    return False

def positions(lines,row,col,direction):
    positions_l = []

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if [i,j] == [row,col] or lines[i][j] != '.':
                continue
            clines = [line[:] for line in lines]
            clines[i][j] = '#'
            if looping(clines,row,col,direction):
                positions_l.append([i,j])
    return len(positions_l)


with open("dataaoc6.txt",'r') as f:
    lines = [list(line.strip()) for line in f.readlines()]

for i in lines:
    if '^' in i:
        print(positions(lines,lines.index(i),i.index('^'),'^'))
        break
    if '>' in i:
        print(positions(lines,lines.index(i),i.index('>'),'>'))
        break
    if 'v' in i:
        print(positions(lines,lines.index(i),i.index('v'),'v'))
        break
    if '<' in i:
        print(positions(lines,lines.index(i),i.index('<'),'<'))
        break