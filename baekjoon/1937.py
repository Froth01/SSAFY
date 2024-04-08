import sys
sys.setrecursionlimit(250000)
input = sys.stdin.readline

def dfs(i,j,area):
    global max_bamboo
    for d in range(4):
        di,dj = i+delta[d][0], j+delta[d][1]
        if di<0 or di>N-1 or dj<0 or dj>N-1 or visited[di][dj]:
            if max_bamboo < area:
                max_bamboo = area
        elif not visited[di][dj] and frame[di][dj] > frame[i][j]:
            if possible[di][dj]:
               max_bamboo = max(max_bamboo,possible[di][dj]+area)
            else :
                visited[di][dj] = 1
                dfs(di,dj,area+1)
                visited[di][dj] = 0


N = int(input())
frame = [list(map(int,input().split())) for _ in range(N)]
possible = [[0]*N for _ in range(N)]
visited = [[0]*N for _ in range(N)]
delta = [(0,1),(1,0),(0,-1),(-1,0)]
result = 0
for i in range(N):
    for j in range(N):
        max_bamboo = 0
        visited[i][j] = 1
        dfs(i,j,1)
        visited[i][j] = 0
        if not possible[i][j]:
            possible[i][j] = max_bamboo
        visited[i][j] = 0
        result = max(max_bamboo,result)
print(result)