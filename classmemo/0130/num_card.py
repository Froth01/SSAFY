import sys
sys.stdin = open('sample_input (2).txt')

T = int(input())
for t in range(T):
    N = int(input())
    card = list(map(int,str(input())))
    max_cnt = 0
    COUNTS = [0]*(9+1)
    for i in range(len(card)):
        COUNTS[card[i]]+=1
    for c in range(len(COUNTS)-1,-1,-1):
        if max_cnt<COUNTS[c]:
            max_cnt=COUNTS[c]
            max_index=c
    print(f'#{t+1} {max_index} {max_cnt}')