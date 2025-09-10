def cross(lines):
    cross = 0
    for j in range(len(lines)-2):
        for i in range(len(lines[j])-2):
            if ((lines[j][i],lines[j+1][i+1],lines[j+2][i+2])==('M','A','S')) or ((lines[j][i],lines[j+1][i+1],lines[j+2][i+2])==('S','A','M')):
                if ((lines[j+2][i],lines[j+1][i+1],lines[j][i+2])==('M','A','S')) or ((lines[j+2][i],lines[j+1][i+1],lines[j][i+2])==('S','A','M')):
                    cross +=1
    return cross

f = open("dataaoc4.txt",'r')
lines = [list(line.strip()) for line in f.readlines()]

print(cross)
