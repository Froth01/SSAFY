T = int(input())
for t in range(T):
    paper = [[0]*10 for _ in range(10)]
    paint = []
    N = int(input())
    for n in range(N):
        paint.append(list(map(int,input().split())))
        for i in range(paint[n][0],paint[n][2]+1):
            for j in range(paint[n][1],paint[n][3]+1):
                if paper[i][j]!=paint[n][4]:
                    paper[i][j]+=paint[n][4]
    purple = 0
    for r in range(10):
        for c in range(10):
            if paper[r][c]>=3:
                purple+=1
    print(f'#{t+1} {purple}')
