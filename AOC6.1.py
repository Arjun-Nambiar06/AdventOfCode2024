def move(lines,row,col,count,direction):
    if direction == '^':
        while row >= 0 and lines[row][col]!='#':
            if lines[row][col] != 'X':
                count += 1
                lines[row][col] = 'X'
            row -= 1
        if row<0:
            return count
        elif lines[row][col]=='#':
            return move(lines,row+1,col,count,'>')
    if direction == '>':
        while col < len(lines[0]) and lines[row][col]!='#':
            if lines[row][col] != 'X':
                count += 1
                lines[row][col] = 'X'
            col += 1
        if col>=len(lines[0]):
            return count
        elif lines[row][col]=='#':
            return move(lines,row,col-1,count,'v')
    if direction == 'v':
        while row < len(lines) and lines[row][col]!='#':
            if lines[row][col] != 'X':
                count += 1
                lines[row][col] = 'X'
            row += 1
        if row>=len(lines):
            return count
        elif lines[row][col]=='#':
            return move(lines,row-1,col,count,'<')
    if direction == '<':
        while col >= 0 and lines[row][col]!='#':
            if lines[row][col] != 'X':
                count += 1
                lines[row][col] = 'X'
            col -= 1
        if col<0:
            return count
        elif lines[row][col]=='#':
            return move(lines,row,col+1,count,'^')


with open("dataaoc6.txt",'r') as f:
    lines = [list(line.strip()) for line in f.readlines()]

count = 0
for i in lines:
    if '^' in i:
        print(move(lines,lines.index(i),i.index('^'),count,'^'))
        break
    if '>' in i:
        print(move(lines,lines.index(i),i.index('>'),count,'>'))
        break
    if 'v' in i:
        print(move(lines,lines.index(i),i.index('v'),count,'v'))
        break
    if '<' in i:
        print(move(lines,lines.index(i),i.index('<'),count,'<'))
        break