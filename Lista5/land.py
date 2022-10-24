nCases = int(input())
for i in range(0,nCases):
    n = int(input())
    a = n * (n-1)/2
    f = a  + 2 -n
    print(f - 1 + n)