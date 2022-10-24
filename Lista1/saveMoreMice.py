nCasos =  int(input())
for i in range(0,nCasos):
    fim, _ = map(lambda x: int(x),input().split(" "))
    posRatos =  list(map(lambda x: int(x), input().split(" ")))
    posRatos.sort(reverse=True)
    posGato =  0
    ratosSalvos= 0
    for posRato in posRatos:
        if posRato > posGato:
            ratosSalvos+=1
            posGato+= fim - posRato
    print(ratosSalvos)
