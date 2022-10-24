nCasos = int( input())
for i in range(0,nCasos):
    entrada = input()
    mapa = {}
    count = 0
    for j in range(97,123):
        mapa[chr(j)] = [0,None]
    mapaOrigin = mapa
    for j in range (0, len(entrada)):
        letra = entrada[j]
        mapa[letra][0] +=1
        for k in range(j+1,len(entrada)):
            mapa[entrada[k]][0]+=1
            mapa[entrada[k]][1] = k if mapa[entrada[k]][1] == None else mapa[entrada[k]][1]
            if mapa[letra][0]==2:
                count += k-1-j
            elif mapa[entrada[k]][0]==2:
                count += mapa[entrada[k]][1] - j
    print(count)



