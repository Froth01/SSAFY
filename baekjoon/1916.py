import sys
input = sys.stdin.readline

def lowest_cost(s,e,costs,frame,adjl,visited,sum_cost):
    if s == e:
        costs.append(sum_cost)
        return
    else:
        for i in adjl[s]:
            if i not in visited:
                visited.add(i)
                sum_cost+=frame[s][i]
                lowest_cost(i,e,costs,frame,adjl,visited,sum_cost)
                sum_cost-=frame[s][i]
                visited.remove(i)

N = int(input())
M = int(input())
frame = [[100000]*(N+1) for _ in range(N+1)]
adjl = [[] for _ in range(N+1)]
visited = set()
costs = []
for m in range(M):
    start,end,cost = map(int,input().split())
    adjl[start].append(end)
    if cost<frame[start][end]:
        frame[start][end]=cost
start,end = map(int,input().split())
visited.add(start)
lowest_cost(start,end,costs,frame,adjl,visited,0)
costs.sort()
print(costs[0])


