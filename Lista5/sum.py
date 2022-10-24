from math import floor


nCases = int(input())
for i in range(0,nCases):
    s= input()
    n = int(s)
    if(s[-1] == "9"):
        print(floor((n+1)/10))
    else:
        print(floor(n/10))