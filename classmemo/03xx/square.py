def route_search(start_y,start_x):
    global cnt
    for d in range(4):
        di = start_y + dti[d]
        dj = start_x + dtj[d]
        if 0>di or di>N-1 or 0>dj or dj>N-1:
            continue
        elif frame[start_y][start_x]+1==frame[di][dj]:
            cnt += 1
            route_search(di,dj)
    return

T = int(input())
for t in range(T):
    N = int(input())
    frame = [list(map(int,input().split())) for _ in range(N)]
    dti = [0,1,0,-1]
    dtj = [1,0,-1,0]
    length = [[0]*N for _ in range(N)]
    max_lst = []
    max_length = 0
    for i in range(N):
        for j in range(N):
            cnt = 1
            route_search(i,j)
            length[i][j]=cnt
            if max_length<length[i][j]:
                max_length=length[i][j]
    for i in range(N):
        for j in range(N):
            if length[i][j]==max_length:
                max_lst.append(frame[i][j])
    print(f'#{t+1}',end=' ')
    print(min(max_lst),max_length)