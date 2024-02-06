num = list(map(int,input().split()))
num.sort()
yack = []
A,B = num
while True:
    for p in range(A,-1,-1):
        if A%p==0 and B%p==0:
            yack.append(p)
            A//=p
            B//=p
    if 
    for y in yack:
        G *= y
    L = G * A * B
    break
print(G)
print(L)