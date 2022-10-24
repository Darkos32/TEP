n  =int(input())
for _ in range(0,n):
    y = input()
    soma = 0
    has0 =False
    hasPar = False
    for c in y:
        soma+=int(c)
        if c =="0" and not has0:
            has0 = True
            continue
        elif int(c)%2==0:
            hasPar = True
    if has0 and hasPar and soma%3==0:
        print("red")
    else:
        print("cyan")
