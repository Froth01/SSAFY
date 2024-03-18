

N = int(input())
frame = [[0]*N for _ in range(N)]
for i in range(N):
        frame[i][N-1-i]=frame[i][i]=1
