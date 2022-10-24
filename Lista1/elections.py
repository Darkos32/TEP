nCasos = int(input())
for i in range(0,nCasos):
    entrada = list(map(lambda x: int(x),input().split(" ")))
    maior = 0
    count = 0
    for j in entrada:
        if j > maior:
            maior = j
            count = 0
        elif j== maior:
            count +=1
    saida = ""
    for j in entrada:
        if j == maior and count>0:
            saida+="1 "
        elif j == maior:
            saida+= "0 "
        else:
            saida += str(maior - j +1)+ " "
    print(saida)
