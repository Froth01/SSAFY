N,M = map(int,input().split())
frame = [input() for _ in range(N)]
chess = [
['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW'],
['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
]
min_val = 64
for r in range(2):
    for i in range(N-7):
        for j in range(M-7):
            cnt = [0,0]
            for ii in range(8):
                for jj in range(8):
                    if frame[i+ii][j+jj]!=chess[r][ii][jj]:
                        cnt[r]+=1
            if min_val>cnt[r]:
                min_val=cnt[r]
print(min_val)