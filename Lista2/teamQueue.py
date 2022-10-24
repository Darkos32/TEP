contador= 0
nFilas = -1
while nFilas !=0:
    contador+=1
    nFilas  = int(input())
    if(nFilas == 0):
        break
    equipes = {}
    count = 1
    fila = []
    for i in range(0,nFilas):
        entrada = input()
        team = list(map(lambda x : int("0"+x),entrada.split(" ")[1:len(entrada)]))
        equipes[count]= [team,False,[]]
        count += 1 
    saida = []
    print("Scenario #" + str(contador))
    while True:
        comando=  input().split(" ")
        if len(comando) >1:
            elemento = comando[1]
            comando = comando[0]
            
        else:
            comando = comando[0]
        if comando =="STOP":
            break
        elif comando =="ENQUEUE":
            for equipe in equipes.values():
                if equipe[2]==[]:
                    equipe[1]=False
                if equipe[0].count(int(elemento)) >0:
                    if not equipe[1]:
                        fila.append(equipe[2])
                        equipe[1] =True
                    equipe[2].append(elemento)
                    break
        elif comando =="DEQUEUE":
            
            print(fila[0].pop(0))
            if fila[0] == []:
                fila.pop(0)
              
    print()     
        

