def valid(text,find):
    find+=4
    dig = False
    d1 = 0
    d2 = 0
    while find < len(text) and text[find].isdigit():
        dig = True
        d1 = d1*10 + int(text[find])
        find+=1
    if dig != True:
        return False
    dig = False
    if text[find] == ',':
        find+=1
        while find < len(text) and text[find].isdigit():
            dig = True
            d2 = d2*10 + int(text[find])
            find+=1
        if text[find] == ')':
            return d1*d2
    return False         

with open("dataaoc3.txt",'r') as f:
    text = f.read()
    length = len(text)
    find = 0
    sum = 0
    dont_st = 0
    can_do = True
    while find != -1:
        dont = text.find("don't()",find)
        if dont == -1:
            dont = length - 1 
        
        do = text.find("do()",find)
        if do == -1:
            do = length - 1 
            
        find = text.find("mul(",find)
        if find == -1:
            break
        if dont < find < do:
            can_do = False
        if do < find < dont:
            can_do = True
        if can_do == True:
            Valid = valid(text,find)
            if Valid != False:
                sum += Valid
        find+=4
print(sum)