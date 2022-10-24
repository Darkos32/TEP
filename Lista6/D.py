
from random import randint


aux = {}
maior = -1
for i in range(2, 65001):
    if aux.setdefault(i, -1) == -1:

        for j in range(i*i, 65001, i):
            aux[j] = 0

while True:
    n = int(input())
    if n == 0:
        break

    if aux[n] == -1:
        print(str(n) + " is normal.")
    else:
        a = randint(2,n-1)
        flag = False if (a**n)% n!=a else True
        if flag:
            print("The number " + str(n) + " is a Carmichael number")
        else:
            print(str(n) + " is normal.")
