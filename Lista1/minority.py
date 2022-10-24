nCasos = int(input())
for i in range(0,nCasos):
    entrada = input()
    tam =len(entrada)
    while True:
        mapa = {'0': 0,'1':0}
        for j in range(0,tam):
            char =  entrada[j]
            mapa[char]+=1
        if mapa['0']*mapa['1']!=0:
            if mapa['0']>mapa['1']:
                print(mapa['1'])
                break
            elif mapa['0'] < mapa['1']:
                print(mapa['0'])
                break
            tam -= 1
        else:
            print(0)
            break