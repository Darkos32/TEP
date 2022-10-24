while True:
    try:
        n = int(input())
        if n % 2 !=0:
            if n - 3 < 6:
                print("Impossible")
            
    except EOFError:
        break
