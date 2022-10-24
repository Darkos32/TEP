n = input()
doisUltimos = n[-2] +  n[-1] if len(n)>= 2 else n[-1]
doisUltimos = int(doisUltimos)
resultado = 0
exp = doisUltimos % 4
for i in range(1,5):
    resultado+= (i** exp) 
resultado = resultado %5
print(resultado)

