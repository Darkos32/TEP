
tam = int(input())
string  = input()
nQueries = int(input())
for i in range(0,nQueries):
    entrada = input().split(" ")
    entrada = list( map(lambda x: int("0" +x),entrada))
    inicio1,inicio2,tamanho = entrada[0:3]
    sub1 = string[inicio1 - 1: inicio1 -1  + tamanho]
    sub2 = string[inicio2 - 1: inicio2  -1+ tamanho]
    