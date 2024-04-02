import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
frame = [[0]*N for _ in range(N)]
turn = {}
delta = [(0,1),(1,0),(0,-1),(-1,0)] # delta의 idx가 증가하면 오른쪽으로 돈다
K = int(input())
for k in range(K):
    i,j = map(int,input().split())
    frame[i-1][j-1] = 2
L = int(input())
for l in range(L):
    num,d = input().split()
    turn[int(num)] = d
s = 0
d = 0
i = j = 0
frame[0][0] = 1
route = deque([(0,0)])
while True:
    di = i + delta[d][0]
    dj = j + delta[d][1]
    if di<0 or di>=N or dj<0 or dj>=N or (di,dj) in route:
        break
    elif frame[di][dj] != 2:
        ii,jj = route.popleft()
        frame[ii][jj] = 0
    frame[di][dj] = 1
    i,j = di,dj
    route.append((di,dj))
    s += 1
    if s in turn.keys():
        if turn[s] == 'D':
            d = (d+1)%4
        else:
            if d==0:
                d = 3
            else:
                d -= 1
print(s+1)
