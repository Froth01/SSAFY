
def DFS(x,y,past):
    global cnt
    change = False
    for d in range(4):
        di = x+dti[d]
        dj = y+dtj[d]
        if di<0 or di>R-1 or dj<0 or dj>C-1:
            continue
        elif frame[di][dj] not in past and not visited[di][dj]:
            change=True
            visited[di][dj]=1
            cnt+=1
            past+=str(frame[di][dj])
            DFS(di,dj,past)
            past=past[:-1]
            cnt-=1
    if not change:
        route.append(cnt)

R,C = map(int,input().split())
frame = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
dti = [0,1,0,-1]
dtj = [1,0,-1,0]
route = []
cnt=1
past = str(frame[0][0])
DFS(0,0,past)
print(max(route))