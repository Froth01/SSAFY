import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def bfs(num,finish):
    global cnt, possibility,visited
    if num == finish:
        possibility.append(cnt)
        cnt = 0
        return min(possibility)
    elif 2*num < finish:
        cnt+=1
        bfs(2*num,finish)
    else:
        if 2*(num+1)<=K:
            cnt+=1
            bfs(num+1,finish)
        else:
            cnt-=1
            bfs(num-1,finish)

N,K = map(int,input().split())
possibility=[]
visited = []
cnt = 0
print(bfs(N,K))
