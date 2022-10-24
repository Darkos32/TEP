numeroCasos = int(input())

for i in range(0, numeroCasos):
    tamVetor = int(input())
    entrada = input().split(" ")
    entrada = list(map(lambda x: int(x), entrada))
    maior = 0
    segundoMaior = 0
    for j  in entrada:
        if j >= maior:
            segundoMaior = maior
            maior = j
        elif j>= segundoMaior:
            segundoMaior = j
    if maior - segundoMaior >1:
        print("NO")
    else:
        print("YES")
