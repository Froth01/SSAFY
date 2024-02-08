import sys
input = sys.stdin.readline
import heapq

N = int(input())
min_heap=[]
for n in range(N):
    num = int(input())
    if num==0:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, num)