import csv

def findvalue(target,data,value,i):
    if i == len(data):
        return value==target
    return findvalue(target,data,value+data[i],i+1) or findvalue(target,data,value*data[i],i+1)


with open("valuesaoc7.csv", 'r') as f:
    rdr = csv.reader(f)
    sum = 0
    for row in rdr:
        data = [int(i.strip()) for i in row if i.strip().isdigit()]
        
        if findvalue(data[0],data,0,1):
            sum += data[0]
print(sum)