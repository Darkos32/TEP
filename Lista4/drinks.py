
from bisect import bisect
from math import floor

try:
    n = int(input())
    valores = []

    valores = list(map(lambda x: int(x), input().split(" ")))
    q = int(input())
    valores = sorted(valores)
    flag = None
    pivo = None
    for i in range(0, q):
        valor = int(input())
        print(bisect(valores,valor))


except EOFError:
    pass
