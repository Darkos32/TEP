mapa = {1:1}
def golomb(n):
    if n in mapa:
        return mapa[n]
    else:
        novo = 1 + golomb(n - golomb(golomb(n-1)))
        mapa[n] = novo
        return novo 
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(1,n+1):
        pass
    print("fim")