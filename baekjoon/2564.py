import sys
input = sys.stdin.readline
from collections import deque

garo,sero = map(int,input().split())
frame = [[0]*(garo+1) for _ in range(sero+1)]
way = deque()
N = int(input())

for n in range(1,N+2):
    i,j = map(int,input().split())
    if i==1:
        frame[0][j] = n
    elif i==2:
        frame[sero][j] = n
    elif i==3:
        frame[j][0] = n
    elif i==4:
        frame[j][garo] = n

for g in range(garo+1):
    way.append(frame[0][g])
way.pop()
for s in range(sero+1):
    way.append(frame[s][-1])
way.pop()
for g in range(garo,-1,-1):
    way.append(frame[-1][g])
way.pop()
for s in range(sero,-1,-1):
    way.append(frame[s][0])
way.pop()

while way[0]!=N+1:
    way.rotate(1)
way.rotate(1)
result = [[0,0] for _ in range(N+1)]

distance = 1
for n in range(N):
    while way[0]==0:
        way.rotate(1)
        distance+=1
    result[way[0]][0]=distance+n
    way.rotate(1)
while way[0]!=N+1:
    way.rotate(1)
way.rotate(-1)
distance = 1
for n in range(N):
    while way[0]==0:
        way.rotate(-1)
        distance+=1
    result[way[0]][1]=distance+n
    way.rotate(-1)

answer = 0
for r in result:
    answer+=min(r)
print(answer)

