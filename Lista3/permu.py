while True:
    try:
        mapa1 = {}
        mapa2 = {}
        for i in range(97,123):
            mapa1[chr(i)] = 0
            mapa2[chr(i)] = 0
        s1 = input()
        s2 = input()
        saida = ""
        for s in s1:
            mapa1[s]+=1
        for s in s2:
            mapa2[s]+=1
        for i in range(97,123):
            if mapa1[chr(i)]*mapa2[chr(i)]>0:
                minimo = min(mapa1[chr(i)],mapa2[chr(i)])
                for j in range(0,minimo):
                    saida+=chr(i)
        print(saida)
    except EOFError:
        break