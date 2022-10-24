from math import ceil, floor
from statistics import median
from tabnanny import verbose


n = int(input())
for i in range(0,n):
    vetor = input().split(" ")
    r =  int(vetor.pop(0))
    vetor = list(map(lambda x:int(x),vetor))
    vetor = sorted(vetor)
    mediana = None
    meio = floor(r/2)
    if r%2 ==0:
        mediana = (vetor[meio] + vetor[meio -1])/2
    else:
        mediana = vetor[meio]
    soma = 0
    for i in vetor:
        soma += abs(i-mediana)
    print(int(soma))