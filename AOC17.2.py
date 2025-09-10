program = '2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0'.split(",")

def combo(x, regA, regB, regC):
    if int(x) in [0, 1, 2, 3]:
        return int(x)
    elif int(x) == 4:
        return regA
    elif int(x) == 5:
        return regB
    elif int(x) == 6:
        return regC

def test(regA):
    regB, regC = 0, 0
    i = 0
    output = []
    while i < len(program):
        opcode = int(program[i])
        if opcode == 0:
            regA = int(regA / 2**combo(int(program[i+1]), regA, regB, regC))
        elif opcode == 1:
            regB = regB ^ int(program[i+1])
        elif opcode == 2:
            regB = combo(int(program[i+1]), regA, regB, regC) % 8
        elif opcode == 3:
            if regA != 0:
                i = int(program[i+1])
                continue
        elif opcode == 4:
            regB = regB ^ regC
        elif opcode == 5:
            output.append(combo(int(program[i+1]), regA, regB, regC) % 8)
        elif opcode == 6:
            regB = int(regA / 2**combo(int(program[i+1]), regA, regB, regC))
        elif opcode == 7:
            regC = int(regA / 2**combo(int(program[i+1]), regA, regB, regC))
        i += 2
    return output

i = 2
store = []
integral_program = [int(x) for x in program]
for j in range(7,-1,-1):
    if test(j) == integral_program[-1:]:
        store.append([j,2])
while i <= len(program)+1:
    if not store:
        break
    j = store.pop()
    i = j[1]
    for regA in range(int(str(bin(j[0])[2:])+'000',2)+7,int(str(bin(j[0])[2:])+'000',2)-1,-1):
        if test(regA) == integral_program:
            print(regA)
        elif test(regA) == integral_program[-i:]:
            store.append([regA,i+1])
    i += 1
