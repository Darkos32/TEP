while True:
    try:
        n, m = list(map(lambda x: int(x), input().split()))
        if m< n:
            print(str(m)+" divides " + str(n)+"!")
        else:
            fatorial =  list( range(2,n+1))
            k = m
            for f in fatorial:
                if m % f == 0:
                    k = m/f
                    if k ==1:
                        break
            if k==1:
                print(str(m)+" divides " + str(n)+"!")
            else:
                print(str(m)+" does not divide " + str(n)+"!")
    except EOFError:
        break
