nCasos = int(input())
for i in range(0,nCasos):
    string = input()
    x = int(input())
    
    tam = len(string)
    saida = ["1"] * tam
    for j in range(0,tam):
        if string[j] == "0":
            if j+x < tam:
                saida[j+x] = "0"
            if j-x >= 0:
                saida[j-x] = "0"
        else:
            if not  (j-x >= 0 and saida[j-x] =="1") or (j+x < tam and saida[j+x] =="1"):
                saida = ["-1"]
                break
    print("".join(saida))