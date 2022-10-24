

while True:
    n = int(input())
    if n == 0:
        break
    aux = {}
    maior = -1
    for i in range(2, n+1):
        if aux.setdefault(i, -1) == -1:
            if i != n and n % i == 0:
                maior = i
            for j in range(i*i, n+1, i):
                aux[j] = 0
    print(maior)
