
from math import floor




nCasos = int(input())
for _ in range(0, nCasos):
    n, m = list(map(lambda x: int(x), input().split(" ")))
    saida = 0
    while n !=0 or m != 0 :
        saida += m-n
        m= int(floor(m/10))
        n = int(floor(n/10))
    print(saida)
