import heapq

N,M,k = map(int,input().split())
frame = [list(map(int,input().split())) for _ in range(N)]
smell = [[0]*N for _ in range(N)]
shark_head = list(map(int,input().split()))
move = [[list(map(int,input().split())) for _ in range(4)] for _ in range(M)]
queue = []
dti = [0,-1,1,0,0]
dtj = [0,0,0,-1,1]
for i in range(N):
    for j in range(N):
        if frame[i][j]!=0:
            smell[i][j]=[frame[i][j],k]
            queue.append([frame[i][j],shark_head[frame[i][j]-1],i,j])
time = 0
move_lst = []

while queue:
    q = queue.pop(0)
    trigger = False
    for d in range(4):
        di = q[2]+dti[move[q[0]][q[1]][d]]
        dj = q[3]+dtj[move[q[0]][q[1]][d]]
        if di>N-1 or di<0 or dj>N-1 or dj<0 :
            continue
        elif frame[di][dj]==0:
            trigger = True
            move_lst.append([q[0],di,dj])
            frame[q[2]][q[3]]=0
            break
    if not trigger:
        for d in range(4):
            di = q[2]+dti[move[q[0]][q[1]][d]]
            dj = q[3]+dtj[move[q[0]][q[1]][d]]
            if di>N-1 or di<0 or dj>N-1 or dj<0:
                continue
            elif smell[di][dj][0]==q[0]:
                move_lst.append([q[0],di,dj])
                frame[q[2]][q[3]] = 0
                break
while move_lst:
    m = move_lst.pop(0)
    if frame[[m[1]][m[2]]>m[0]:

    frame[m[1]][m[2]]=m[0]