import sys
input = sys.stdin.readline
import heapq

N = int(input())
abs_heap=[]
for n in range(N):
    num = int(input())
    if num==0:
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(abs_heap,(abs(num),num))
