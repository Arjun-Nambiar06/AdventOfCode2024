def horizontal(lines):
    hori = 0
    for line in lines:
        for i in range(len(line)-3):
            if ((line[i],line[i+1],line[i+2],line[i+3])==('X','M','A','S')) or ((line[i],line[i+1],line[i+2],line[i+3])==('S','A','M','X')):
                hori += 1
    return hori

def vertical(lines):
    verti = 0
    for j in range(len(lines)-3):
        for i in range(len(lines[j])):
            if ((lines[j][i],lines[j+1][i],lines[j+2][i],lines[j+3][i])==('X','M','A','S')) or ((lines[j][i],lines[j+1][i],lines[j+2][i],lines[j+3][i])==('S','A','M','X')):
                verti +=1
    return verti

def diagonal(lines):
    dia = 0
    for j in range(len(lines)-3):
        for i in range(len(lines[j])-3):
            if ((lines[j][i],lines[j+1][i+1],lines[j+2][i+2],lines[j+3][i+3])==('X','M','A','S')) or ((lines[j][i],lines[j+1][i+1],lines[j+2][i+2],lines[j+3][i+3])==('S','A','M','X')):
                dia +=1
    return dia

def anti_diagonal(lines):
    a_dia = 0
    for j in range(3,len(lines)):
        for i in range(len(lines[j])-3):
            if ((lines[j][i],lines[j-1][i+1],lines[j-2][i+2],lines[j-3][i+3])==('X','M','A','S')) or ((lines[j][i],lines[j-1][i+1],lines[j-2][i+2],lines[j-3][i+3])==('S','A','M','X')):
                a_dia +=1
    return a_dia


f = open("dataaoc4.txt",'r')
lines = [list(line.strip()) for line in f.readlines()]

print(horizontal(lines)+vertical(lines)+diagonal(lines)+anti_diagonal(lines))
