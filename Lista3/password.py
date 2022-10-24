while True:
    try:
        mapa = {}
        n, s = input().split(" ")
        n = int(n)
        for i in range(0,len(s)):
            sub = ""
            for j in range(0,n):
                if i + j<len(s):
                    sub+=s[i+j]
            mapa[sub] = mapa.setdefault(sub,0) + 1
        vetor = sorted(mapa,key=mapa.get,reverse=True)
        print(vetor[0])
    except EOFError:
        break