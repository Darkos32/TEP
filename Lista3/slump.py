
def slump(string):
    if len(string) <3:
        return False
    if string[0] !="D" and string[0]!="E":
        return False
    if string[1]!="F":
        return False
    index = 1
    while  index < len(string) and string[index]=="F":
        index+=1
    resto = string[index if index < len(string) else len(string) - 1:]
    if len(resto) == 1:
        if resto[0]!="G":
            return False
    else:
        if(not slump(resto)):
            return False
    return True

def slimp(string):
    if len(string)<2:
        return False
    if string[0]!="A":
        return False
    if len(string) ==2:
        if string[1]=="H":
            return True
        else:
            return False
    else:
        if string[-1] != "C":
            return False
        else:
            if string[1]=="B" and slimp(string[2:len(string)-1]):
                return True
            elif slump(string[1:len(string) -1]):
                return True
            else:
                return False
def slurpy(string):
    if len(string)<5:
        return False
    for tam in range(2,len(string)):
        sub1 = string[0:tam]
        sub2 = string[tam:]
        if slimp(sub1) and slump(sub2):
            return True
    return False
n = int(input())
print("SLURPYS OUTPUT")
for i in range(0,n):
    entrada= input()
    if slurpy(entrada):
        print("YES")
    else:
        print("NO")
print("END OF OUTPUT")