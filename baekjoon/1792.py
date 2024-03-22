def GCD(x,y):
    if x < y:
        x,y = y,x
    while y>0 :
        x,y = y,x%y
    return x

T = int(input())
for t in range(T):
    a,b,d = map(int,input().split())
    gcds = [[0]*50001 for _ in range(50001)]
    for x in range(1,a+1):
        for y in range(1,b+1):
            if gcds[x][y] or gcds[y][x] :
                continue
            else:
                gcds[x][y] = gcds[y][x] = GCD(x,y)