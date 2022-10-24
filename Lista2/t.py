def mySplit(string):
    temp = ""
    vetor = []
    for char in string:
       if char == " ":
            vetor.append(temp)
            temp = ""
       else:
            temp += char
    vetor.append(temp)
    if vetor[-1] =='':
        vetor.pop()
    return vetor

print(mySplit(input()))