import sys
input = sys.stdin.readline
import heapq

T = int(input())
for t in range(T):
    Q = []
    k = int(input())
    for _ in range(k):
        command = input().split()
        if command[0]=='I':
            heapq.heappush(Q,int(command[1]))
        elif command[0]=='D':
            if Q:
                if command[1] == '1':
                    max_val = max(Q)
                    Q.remove(max_val)
                else:
                    heapq.heappop(Q)
    if len(Q)==0:
        print('EMPTY')
    else:
        print(max(Q), heapq.heappop(Q))
