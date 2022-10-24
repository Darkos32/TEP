from math import floor


nCases = int(input())
for i in range(0,nCases):
    inicio,fim =  list(map(lambda x: int(x), input().split(" ")))
    soma = fim - inicio
    
    while floor(fim/10)>0:
        soma +=1
        fim = floor(fim/10)
    print(soma)
