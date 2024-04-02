from heapq import heappop,heappush
import sys
input = sys.stdin.readline

def dijkstra(start_i,start_j):
    pq = []
    heappush(pq,[0,start_i,start_j])
    thief[start_i][start_j]=frame[start_i][start_j]
    while pq:
        minus,i,j = heappop(pq)
        for d in range(4):
            di,dj = i+delta[d][0], j+delta[d][1]
            if di<0 or di>=N or dj<0 or dj>=N:
                continue



case = 1
inf = int(1e9)
while True:
    N = int(input())
    if N == 0:
        break
    frame = [list(map(int,input().split())) for _ in range(N)]
    thief = [[inf]*N for _ in range(N)]
    delta = [(0,1),(1,0),(0,-1),(-1,0)]



