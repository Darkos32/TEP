


n = int(input())
vetor = list(map(lambda x: int(x), input().split(" ")))
right = True
left = True
for i  in range(0,n-1):
    if vetor[i+1]<= vetor[i]:
        break
    left = not left
for j in range(n-1,-1,-1):
    if vetor[j-1] <= vetor[j]:
        break
    right= not right
if right or left:
    print("Alice")
else:
    print("Bob")