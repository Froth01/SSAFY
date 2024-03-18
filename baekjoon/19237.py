N,M,k = map(int,input().split())
frame = [list(map(int,input().split())) for _ in range(N)]
shark_head = list(map(int,input().split()))
shark = [[] for _ in range(M)]
move = [[] for _ in range(M)]

dti = [-1,1,0,0]
dtj = [0,0,-1,1]

for i in range(M):
    for _ in range(4):
        move[i].append(list(map(int,input().split())))


for i in range(N):
    for j in range(N):
        if frame[i][j] != 0:
            shark[frame[i][j]-1] = [i,j,shark_head[frame[i][j]-1]-1]
        frame[i][j]=[0,0]

def smell(lst,shark):
    for i in range(len(shark)):
        if shark[i]:
            x,y,d = shark[i]
            lst[x][y]=[k,i]
    return lst

def next(lst):
    for i in range(N):
        for j in range(N):
            if lst[i][j][0]>0:
                lst[i][j][0] -= 1
    return lst

def moving(shark):
    way = [[[] for _ in range(N)] for r in range(N)]
    for i in range(len(shark)):
        if shark[i]:
            x,y,m = shark[i]
            route = []
            my_route = []
            for k in range(4):
                nx,ny = x+dti[k], y+dtj[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if frame[nx][ny][0] == 0:
                        route.append((nx,ny,k))
                    elif frame[nx][ny][1] == i:
                        my_route.append((nx,ny,k))
            new_way = m
            if not route:
                route = my_route
            if len(route) >= 2:
                shark_rank = move[i][m]
                for r in shark_rank:
                    trigger = False
                    for a,b,c in route:
                        if r-1 == c:
                            new_way = r - 1
                            trigger = True
                            break
                    if trigger:
                        break
            else:
                new_way = route[0][2]
            shark[i]=[x+dti[new_way], y+dtj[new_way], new_way]
            way[x+dti[new_way]][y+dtj[new_way]].append(i)

    for i in range(N):
        for j in range(N):
            if len(way[i][j])>1:
                way[i][j].sort()
                for k in way[i][j][1:]:
                    shark[k]=[]
    cnt = 0
    for i in range(M):
        if shark[i]:
            cnt+=1
    return shark,cnt

for i in range(1000):
    frame = smell(frame,shark)
    shark, live = moving(shark)
    frame = next(frame)
    if live == 1 :
        print(i+1)
        break
else:
    print(-1)