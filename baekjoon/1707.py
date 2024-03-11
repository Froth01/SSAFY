import sys
input = sys.stdin.readline
from collections import deque

def BFS_check():
    color = [0]*(V+1)
    for i in range(1,V+1):
        if color[i]:
            continue
        else:
            color[i]=1
            queue = deque([i])
            while queue:
                q = queue.popleft()
                for r in adjl[q]:
                    if color[r]==color[q]:
                        return 'NO'
                    elif color[r]==0:
                        if color[q]==1:
                            color[r]=2
                        elif color[q]==2:
                            color[r]=1
                        queue.append(r)
    return 'YES'


T = int(input())
for t in range(T):
    V,E = map(int,input().split())
    adjl = [[] for _ in range(V+1)]
    for e in range(E):
        n1,n2 = map(int,input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)
    if E==1:
        print('YES')
    elif V==1:
        print('NO')
    else:
        print(BFS_check())


