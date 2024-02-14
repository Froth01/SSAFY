N = int(input())
M = int(input())
connection = [[] for _ in range(N+1)]
cnt = 0
for m in range(M):
    connect = map(int,input().split())
    connection[connect[0]]=connection[connect[1]]
    connection[connect[1]]=connection[connect[0]]

def dfs(i): # 시작 i, 마지막 V
    visited = [0]*(N+1)
    stack = []
    visited[i]=1 # 시작점 방문
    while True: # 탐색
        for w in range(len(connection)): # 현재 방문한 정점에 인접하고 방문안한 정점 w
            if visited[w]==0:
                stack.append(i) # push(i), i를 지나서
                i = w           # w에 방문
                visited[w] = 1
                print(i)
                break
            else:           # i에 남은 인접 정점이 없으면
                if stack:   # 스택이 비어있지 않으면(지나온 정점이 남아 있으면)
                    i = stack.pop()
                else:       # 스택이 비어있으면(출발점에서 남은 정점이 없으면)
                    break
    return

