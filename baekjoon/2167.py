N,M = map(int,input().split())
frame = []
for n in range(N):
    frame.append(list(map(int,input().split())))
K = int(input())
for k in range(K):
    total = 0
    source = list(map(int,input().split()))
    for n in range(source[0]-1,source[2]):
        for m in range(source[1]-1,source[3]):
            total+=frame[n][m]
    print(total)