V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjl = [[] for _ in range(V + 1)]  # 인접 리스트 // 행에 i에 인접인 정점번호
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1) # 방향이 없는 경우


def dfs(i,V): # 시작 i, 마지막 V
    visited = [0]*(V+1) # visited, stack 생성 및 초기화
    stack = []
    visited[i]=1 # 시작점 방문
    print(i) # 시작점에서 할일
    while True: # 탐색
        for w in adjl[i]: # 현재 방문한 정점에 인접하고 방문안한 정점 w
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



