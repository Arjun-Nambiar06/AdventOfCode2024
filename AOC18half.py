with open("dataaoc18.txt",'r') as f:
    positions = [line.split(',') for line in f.read().splitlines()]

line = [' ']*71
data = [line[:] for _ in range(71)]
x = 0
for pos in positions:
    if x == 1024:
        break
    data[int(pos[1])][int(pos[0])] = '#'
    x += 1
data[0][0],data[-1][-1] = 'A','B'
datas = []
for line in data:    
    linew = ''
    for i in line:
        linew += i
    linew += '\n'
    datas.append(linew)

with open("dataaoc18text.txt",'w') as f:
    f.writelines(datas)