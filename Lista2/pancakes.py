from math import floor

def flip(vetor,fim):
    for i in range(0,floor(fim/2)):
        hold = vetor[i]
        vetor[i] = vetor[fim - 1-i]
        vetor[fim - i-1 ] =  hold
    return vetor
def verify(vetor):
    for i in range(0,len(vetor)-1):
        for j in range(i+1,len(vetor)):
            if vetor[i]<vetor[j]:
                return False
    else: 
        return True
while True:
    try:
        entrada  = input()
        panquecas = list(map(lambda x: int(x),entrada.split(" ")))
        flips = ""
        tam = len(panquecas)
        limite = tam
        while ((not verify(panquecas)) and ( limite> 1)):
            flag = False
            for i in range(0,limite):
                if panquecas[0]>panquecas[i]:
                    flips+= str(tam - i)+" "
                    panquecas = flip(panquecas,len(panquecas[0:i+1]))
                    flag = True
                    break
            if not flag:
                flip(panquecas,limite)
                flips+=str(tam - limite + 1)+ " "
                limite-=1
                pass
        flips+="1 0"
        panquecas = flip(panquecas,tam)
        print(entrada)
        print(flips)

    except EOFError:
        break