with open("dataaoc8test.txt",'r') as f:
    data = [line.strip() for line in f.readlines()]
    
positions = []
for a in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
    Y = len(data)
    X = len(data[0])
    poss_positions = []
    for i in range(Y):
        for k in range(X):
            if data[i][k] == a:
                poss_positions.append((k,i))
    for i in range(len(poss_positions)):
        for j in range(len(poss_positions)):
                if i!=j:
                    if data[poss_positions[i][1]][poss_positions[i][0]] == data[poss_positions[j][1]][poss_positions[j][0]]:
                        x = -int(poss_positions[i][0])+int(poss_positions[j][0])
                        y = -int(poss_positions[i][1])+int(poss_positions[j][1])
                        if 0 <= -x + int(poss_positions[i][0]) < X and 0 <= -y + int(poss_positions[i][1]) < Y:
                            positions.append((-x + int(poss_positions[i][0]),-y + int(poss_positions[i][0])))
                        if 0 <= int(poss_positions[j][0]) + x < X and 0 <= int(poss_positions[j][1]) + y < Y: 
                            positions.append((int(poss_positions[j][0])+x,int(poss_positions[j][1])+y))
print(len(positions))
print(positions)
                
 
