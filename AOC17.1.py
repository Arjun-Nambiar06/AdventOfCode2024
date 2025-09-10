regA,regB,regC = 47006051,0,0

program = '2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0'.split(",")
def combo(x):
    if int(x) in [0,1,2,3]:
        return int(x)
    elif int(x) == 4:
        return regA
    elif int(x) == 5:
        return regB
    elif int(x) == 6:
        return regC

i = 0
while i < len(program):
    if int(program[i]) == 0:
        regA = int(regA/2**combo(int(program[i+1])))
    elif int(program[i]) == 1:
        regB = regB ^ int(program[i+1])
    elif int(program[i]) == 2:
        regB = combo(int(program[i+1])) % 8
    elif int(program[i]) == 3:
        if regA == 0:
            pass
        else:
            i = int(program[i+1])
            continue
    elif int(program[i]) == 4:
        regB = regB ^ regC
    elif int(program[i]) == 5:
        print(combo(int(program[i+1])) % 8,end=',')
    elif int(program[i]) == 6:
        regB = int(regA/2**combo(int(program[i+1])))
    elif int(program[i]) == 7:
        regC = int(regA/2**combo(int(program[i+1])))
    i+=2