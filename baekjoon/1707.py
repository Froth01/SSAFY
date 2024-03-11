import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    V,E = map(int,input().split())
    adjl = [[] for _ in range(V+1)]
    for e in range(E):
        n1,n2 = map(int,input().split())
        adjl[n1].append(n2)
# 인접리스트까진 받아놨음


