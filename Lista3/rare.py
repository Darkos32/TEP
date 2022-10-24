

anterior = ""
mapa = {}
mapa2 = {}
saida = ""
while True:

    novo = input()
    if novo == "#":
        for v in mapa:
            mapa2[v] = sum((mapa[v].values()))

        while len(mapa) > 0:
            retirado = ""
            for v in mapa2:
                if mapa2[v] == 0:
                    retirado = v
                    saida += v
                    for u in mapa:
                        if v in mapa[u]:
                            mapa2[u] -= 1
                    break

            del mapa2[retirado]
            del mapa[retirado]
        print(saida)
        saida = ""
        break
    if anterior == "":
        anterior = novo
        continue
    for i in range(0, min(len(anterior), len(novo))):
        if anterior[i] != novo[i]:
            if anterior[i] not in mapa:
                mapa[anterior[i]] = {}
            if novo[i] not in mapa:
                mapa[novo[i]] = {}
            mapa[novo[i]][anterior[i]] = 1
            break

    anterior = novo
