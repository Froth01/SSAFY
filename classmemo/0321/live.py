# 간선의 갯수를 최소화하여 모든 정점을 연결
# 1. 여러 가지 방법이 있다.
# 2. 싸이클이 발생하지 않는다.
# 3. 간선의 개수 = V-1 개
# ==> 신장 트리

# 최소 비용 신장 트리
# => 그 중에 비용의 합이 제일 적은 트리

'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
import sys
sys.stdin = open('input.txt','r')

'''PRIM
# 우선순위큐
from heapq import heappush, heappop

def prim(start):
    pq = []
    # 방문 정보
    MST = [0] * V

    # 최소 비용
    sum_weight = 0

    # 시작점 추가
    # 기존 - 노드 번호만 관리 / prim 우선순위가 가중치에 따라 정렬. 관리 데이터 : 노드번호, 가중치
    heappush(pq,(0,start))
    while pq :
        weight, now = heappop(pq)

        # 우선순위 큐 특성상 더 먼거리로 가는 방법이 큐에 저장되어있기 때문에
        # 기존에 이미 더 짧은 거리로 방문했다면 continue
        if MST[now]:
            continue

        MST[now] = 1
        sum_weight += weight

        for to in range(V):
            if graph[now][to] == 0 or MST[to]:
                continue
            heappush(pq,(graph[now][to],to))
    print(f'최소 비용 : {sum_weight}')


V, E = map(int,input().split())
# 인접 행렬
graph = [[0]*V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int,input().split())
    # 무방향그래프라 반대도 저장
    graph[s][e] = w
    graph[e][s] = w
prim(0)
'''

# 1. 전체 그래프를 보고, 가중치가 제일 작은 간선부터 뽑자
# -> 코드로 구현: 전체 간선 정보 저장 + 가중치로 정렬

# 2. 방문 처리 : 싸이클이 발생하면 안된다!

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)

    # 같은 집합이면 pass
    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

V, E = map(int,input().split())
edges = [] # 간선 정보 저장
for _ in range(V):
    s, e, w = map(int,input().split())
    edges.append([s,e,w])
edges.sort(key=lambda x: x[2]) # 가중치를 기준으로 정렬
parents = [i for i in range(V)] # 대표자 배열(자기자신을 바라봄)

sum_weight = 0

# 간선 모두 확인
for s, e, w in edges:
    # 싸이클이 발생하면 pass
    # union-find 이미 같은 집합에 속해 있다면 pass
    if find_set(s) == find_set(e):
        continue
    # 싸이클이 없으면 통과
    union(s,e)
    sum_weight += w
print(f'최소 비용 : {sum_weight}')