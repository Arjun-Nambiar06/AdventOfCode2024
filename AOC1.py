import csv
from math import fabs

l1=[]
l2=[]
sum=0

f=open("valuesaoc1.csv",'r')
rdr=csv.reader(f)
for i in rdr:
    l1.append(int(i[0]))
    l2.append(int(i[1]))

l1.sort()
l2.sort()

for i in range(len(l1)):
    sum += l1[i] * l2.count(l1[i])

print(sum)