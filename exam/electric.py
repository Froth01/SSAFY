def range_home(x,y,dis):
    for d in range(4):
        di = (15+y) + dti[d]
        dj = (15+x) + dtj[d]
        if di<0 or di>30 or dj<0 or dj>30:
            continue
        elif frame[di][dj]==0:
            for _ in range(dis-1):
                range_home(x,y,dis-1)
            frame[di][dj]+=dis-1

T = int(input())
for t in range(T):
    frame = [[0]*31 for _ in range(31)]
    dti = [0,1,0,-1]
    dtj = [1,0,-1,0]
    N = int(input())
    for n in range(N):
        x,y,dis = map(int,input().split())
        range_home(x,y,dis)
    for i in range(31):
        for j in range(31):
            if frame[i][j]>1:


