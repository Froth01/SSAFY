import sys
input = sys.stdin.readline

N = int(input())
frame = [[0]*1001 for _ in range(1001)]
post = [0]*N
for n in range(N):
    paper_x, paper_y, garo, sero = map(int,input().split())
    for i in range(paper_y,paper_y+sero):
        frame[i][paper_x:paper_x+garo]=[n+1]*garo
for i in range(1001):
    for j in range(1001):
        if frame[i][j]!=0:
            post[frame[i][j]-1]+=1
for p in post:
    print(p)