T = int(input())
for t in range(T):
    N,W = map(int,input().split())
    enemy = []
    dt1 = [0,0,-1,1]
    dt2 = [-1,1,0,0]
    for e in range(2):
        enemy.append(list(map(int,input().split())))
    rooms = set()
    go = 0

    for i in range(len(enemy)):
        for j in range(len(list(enemy[i]))):
            gg1 = N*i+j
            effctive = []
            for d in range(4):
                di = i+dt1[d]
                dj = j+dt2[d]
                if di > 1 or di < 0:
                    continue
                else:
                    if dj==N:
                        dj=0
                if enemy[i][j]+enemy[di][dj]<=W:
                    effctive.append([N*i+j,N*di+dj,enemy[i][j]+enemy[di][dj]])

            print(effctive)

