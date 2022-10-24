while True:
    n,m = list(map(lambda x : int(x),input().split(" ")))
    if n == 0 and  m ==0:
        break
    matriz = []
    for i  in range(0,n):
        matriz.append([0]*n)
    for i in range(0,m):
        antes, depois = list(map(lambda x: int(x), input().split(" ")))
        matriz[depois-1][antes-1] = 1
    vetor =  [0] * n
    for i in range(0,n):
        vetor[i] = sum(matriz[i])
    saida = ""
    c = n
    while c>0:
        for i in range(0,n):
            if vetor[i]==0:
                saida += str(i+1)+" "
                for j in range(0,n):
                    if matriz[j][i] ==1:
                        vetor[j]-=1
                vetor[i]= -1
                c-=1
    saida = list(saida)
    saida.pop()
    saida = "".join(saida)
    print(saida)

