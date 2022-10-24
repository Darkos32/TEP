from cmath import sqrt
from math import floor

def sod(n):
    soma = 0
    for i in range(2, floor(sqrt(n).real)+1):
        if n % i == 0:
            soma += n/i + i if n/i !=i else i
    return soma
mapa = {}
while True:
    n = int(input())
    if n == 0:
        break
   
    soma = 0
    for  i in range(1,n+1):
        soma+= sod(i)
    print(soma)