nCasos = int(input())
for i in range(0,nCasos):
    _, tam = list(map(lambda x: int(x), input().split(" ")))
    string = input()
    white = 0
    for j in range(0,tam):
        if string[j] == "W":
            white += 1
    k = 0
    menor = white
    while k + tam < len(string):
        if string[k]=="W":
            white -=1
        if string[k+tam]=="W":
            white+=1
        if white < menor:
            menor = white
        k+=1
    print(menor)
