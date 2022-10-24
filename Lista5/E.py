nCasos = int(input())
for _ in range(0, nCasos):
    tam = int(input(""))
    vetor = list(map(lambda x: int(x), input().split(" ")))
    saida = 0
    vetor = [0] + vetor + [0]
    for i in range(1, tam+1):
        for j in range(vetor[i]-i, tam+1,vetor[i]):
            if j>=0 and i< j and  i+j == vetor[i]*vetor[j]:
                saida += 1

    print(saida)
