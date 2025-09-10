    if data[poss_positions[i][1]][poss_positions[i][0]] == data[poss_positions[j][1]][poss_positions[j][0]]:
                        x = -int(poss_positions[i][0])+int(poss_positions[j][0])
                        y = -int(poss_positions[i][1])+int(poss_positions[j][1])
                        if 0 <= -x + int(poss_positions[i][0]) < X and 0 <= -y + int(poss_positions[i][1]) < Y:
                            positions.append((-x + int(poss_positions[i][0]),-y + int(poss_positions[i][0])))
                        if 0 <= int(poss_positions[j][0]) + x < X and 0 <= int(poss_positions[j][1]) + y < Y: 
                            positions.append((int(poss_positions[j][0])+x,int(poss_positions[j][1])+y))