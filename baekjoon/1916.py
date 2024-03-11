import sys
input = sys.stdin.readline

def lowest_cost(s,e):
    queue = []
    queue.append(s)
    while queue:
        t = queue.pop()
        i
        for i in adjl[t]:
            if i in visited:
                continue
            elif low_cost[i]>frame[t][i]:
                low_cost[i]=frame[t][i]
                visited.add(i)
            else:
                visited.add(i)

N = int(input())
M = int(input())
frame = [[100000]*(N+1) for _ in range(N+1)]
adjl = [[] for _ in range(N+1)]
visited = set()
low_cost = [100000]*(N+1)
for m in range(M):
    start,end,cost = map(int,input().split())
    adjl[start].append(end)
    if cost<frame[start][end]:
        frame[start][end]=cost
start,end = map(int,input().split())
visited.add(start)

print(costs[0])


