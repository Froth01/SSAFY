import sys
input = sys.stdin.readline
import heapq

N = int(input())
min_heap=[]
for n in range(N):
    case = list(map(int,input().split()))
    while case:
        num = case.pop()
        heapq.heappush(min_heap,num)
    while len(min_heap)>N:
        heapq.heappop(min_heap)
print(heapq.heappop(min_heap))
