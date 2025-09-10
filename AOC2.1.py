import csv

total_safe = 0
unsafe = 0

f=open("valuesaoc2.csv",'r')
rdr=csv.reader(f)
for i in rdr:
    iord = 0
    safe = True
    if int(i[0]) < int(i[1]):
        iord = 1
    elif int(i[0]) > int(i[1]):
        iord = -1
    else:
        safe = False
        unsafe += 1
            
    for k in range(len(i)-1):
        if i[k+1] == '':
            continue
        if iord == 1:
            if (int(i[k+1]) - int(i[k]) > 3) or (int(i[k+1]) - int(i[k]) < 1):
                safe = False
                unsafe += 1
                break
        elif iord == -1:
            if (int(i[k]) - int(i[k+1]) > 3) or (int(i[k]) - int(i[k+1]) < 1):
                safe = False
                unsafe += 1
                break
    if safe == True:
        total_safe += 1

print(total_safe)
print(unsafe)

