


def soma(vetor,index):
    if vetor[index] == None:
        return 0
    else:
        return (vetor[index] + soma(vetor,2*index +1), vetor[index] +  soma(vetor,2 *(index+1)))

while True:
    try:
        entrada = ""
        leftBrack = 0
        rightBrack = 0
        while leftBrack != rightBrack or leftBrack*rightBrack == 0:
            novo = input()
            for letra in novo:
                if letra == "(":
                    leftBrack += 1
                elif letra == ")":
                    rightBrack += 1
            entrada += novo
        print(entrada)
        objetivo, _, grafo = entrada.partition(" ")
        objetivo = int(objetivo)
        flag = False
        nos = []
        num = ""
        rightBrack = 0
        ultimoChar = ""
        vetor = []
        for char in grafo:
            if char.isdigit():
                num+= char
            elif char =='(' and num!="":
                vetor.append(int(num))
                num = ""
            elif char == ')' and ultimoChar=='(':
                vetor.append(None)
            ultimoChar = char
        soma = 0
        for i in vetor:
            if i == None and soma == objetivo:
                flag = True
                break
            elif i != None:
                soma += i
            
            
        


    except EOFError:
        break
