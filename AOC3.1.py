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
    find = 0
    sum = 0
    while find != -1:
        find = text.find("mul(")
        if find == -1:
            break
        Valid = valid(text,find)
        if Valid != False:
            sum += Valid
        find+=1
        text = text[find:]
print(sum)
        