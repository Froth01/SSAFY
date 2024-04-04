# BFS 진행시 시간초과
# bfs 지정
def bfs(start):
    queue = []
    # 시작점 삽입
    queue.append((start,0))
    while queue:
        # 현재위치(idx), 뛴 횟수
        now, cnt = queue.pop(0)
        # 현재위치가 마지막점일 경우 종료 - 뛴 횟수 도출
        if now == N-1:
            return cnt
        # 현재위치 값이 0이면 더이상 못뜀 - 케이스 건너뜀
        # 현재위치가 마지막점을 넘어가도 케이스 건너뜀
        elif maze[now] == 0 or now >= N:
            continue
        # 현재위치(idx)의 미로값 경우만큼 queue에 추가
        for n in range(1,maze[now]+1):
            queue.append((now+n,cnt+1))
    # 마지막점에 도달하지 못해 queue가 끝나면 -1 도출
    return -1

# 인접 그래프 제작 함수
def graph_search():
    # 각 정점마다 도착점 지정
    for v in range(N):
        # 정점(idx)위치의 미로값이 0이면 갈수있는 도착점이 없음
        if maze[v]==0:
            continue
        # 그 정점(idx)의 미로 값만큼 다른 곳 들림 - 도착점 추가
        for n in range(1,maze[v]+1):
            # 마지막 점을 넘지 않는 정점만 추가
            if v+n < N:
                graph[v].append(v+n)

#--------------------------------------------
# 도착점 = 마지막점 까지 가는 최솟값 도출 - BFS 이용 - 시간초과
def graph_bfs(start):
    queue = []
    # (시작점,점프횟수)등록
    queue.append((start,0))
    while queue:
        node, jump = queue.pop(0)
        # 현재 정점에서 도착점 순회조사
        for to in graph[node]:
            # 미로값이 0인 정점 통과
            if maze[to]==0:
                continue
            # 마지막 점에 도달하면 jump+1값(도착점이므로 점프 함번 해야함)도출
            # 너비우선이므로 최솟값 도출
            elif to == N-1:
                return jump+1
            # queue에 점프횟수 추가하여 등록
            queue.append((to,jump+1))
    # 마지막점 도달하지 못하면 -1 도출
    return -1
#--------------------------------------------


# 기본정보 입력
N = int(input())
maze = list(map(int,input().split()))

# idx 0에서 출발하는 bfs - 결과값이 직접 도출됨 - 시간초과
# print(bfs(0))

# 인접리스트 지정
# graph = [[] for _ in range(N)]
# graph_search()

# 그래프 bfs - 시간초과
# print(graph_bfs(0))

# 단순하게 규칙찾기...
# idx 0 은 항상 점프 0번, idx 1은 언제나 1(idx0일때는 아예 종료)
# idx 2부터 (전 점프+1,무한대)중 낮은값..
# 마지막 값이 무한대이면, -1로 바꿔 출력 ///// 악랄한 예제;;;;; 1 / 0
minjump = [0]+[int(1e9)]*(N-1)
if maze[0]==0 and len(maze) != 1:
    print(-1)
    exit()
for v in range(N):
    for n in range(1,maze[v]+1):
        if v+n >= N:
            continue
        minjump[v+n]=min(minjump[v]+1,minjump[v+n])
if minjump[-1] == int(1e9):
    print(-1)
else:
    print(minjump[-1])

