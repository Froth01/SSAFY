import sys
sys.stdin = open('input 11.txt')

T = int(input())
for t in range(T):
    N = int(input())
    score = list(map(int,input().split()))
    max_cnt = 0
    COUNTS = [0]*(100+1)
    for i in range(len(score)):
        COUNTS[score[i]]+=1
    for c in range(len(COUNTS)-1,-1,-1):
        if max_cnt<COUNTS[c]:
            max_cnt=COUNTS[c]
            max_idx = c
    print(f'#{t+1} {max_idx}')