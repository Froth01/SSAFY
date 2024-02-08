import sys
input = sys.stdin.readline
import heapq

N = int(input())
max_heap=[]
for n in range(N):
    num = int(input())
    if num==0:
        if max_heap:
            print(heapq.heappop(max_heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(max_heap, (-num,num))