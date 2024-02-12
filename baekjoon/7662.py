import sys
input = sys.stdin.readline
import heapq

T = int(input())
for t in range(T):
    Q_min = []
    Q_max = []
    k = int(input())
    check = [1]*k
    for i in range(k):
        command = input().split()
        if command[0]=='I':
            heapq.heappush(Q_min,(int(command[1]),i))
            heapq.heappush(Q_max,(-int(command[1]),i))
        else:
            if command[1] == '-1':
                if Q_min:
                    check[heapq.heappop(Q_min)[1]] = 0
            elif command[1] == '1':
                if Q_min:
                    check[heapq.heappop(Q_max)[1]] = 0
        while Q_min and check[Q_min[0][1]]==0:
            heapq.heappop(Q_min)
        while Q_max and check[Q_max[0][1]]==0:
            heapq.heappop(Q_max)
    if len(Q_min)==0:
        print('EMPTY')
    else:
        print(-Q_max[0][0], Q_min[0][0])
