n = int(input())
for i in range(0,n):
    nVertices = int(input())
    mapa = {}
    infectados  = 0
    entrada = list(map(lambda x:int(x),input().split(" ")))
    for e in entrada:
        mapa[e] = [ 1 if mapa.get(e,None) == None else mapa[e][0] + 1,0]
    count = 0
    vetor = sorted(mapa,key=lambda x: mapa.get(x)[0],reverse= True)
    print(vetor)
    while infectados <nVertices:
        count +=1
        if infectados == nVertices  - 1:
            infectados+=1
            break
        else:
            maior = None
            for v in mapa:
                if mapa[v][1]>0 and mapa[v][1] + 1 <= mapa[v][0]:
                    mapa[v][1]+=1
                    infectados+=1
                if maior == None or (mapa[maior][0] - mapa[maior][1] < mapa[v][0] - mapa[v][1]):
                    maior = v
            mapa[maior][1]+=1
            infectados+=1
    print(count)


