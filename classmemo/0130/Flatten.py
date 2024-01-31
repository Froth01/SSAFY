import sys
sys.stdin = open('input (4).txt')
for t in range(10):
    work = int(input())
    ground = list(map(int,input().split()))
    max_g = 0
    min_g = 99999
    for g in range(len(ground)):
        if max_g < ground[g]:
            max_g = ground[g]
            max_idx = g
    for g in range(len(ground)):
        if min_g > ground[g]:
            min_g = ground[g]
            min_idx = g
    for w in range(work):
        ground[max_idx]-=1
        ground[min_idx]+=1
        max_g = 0
        min_g = 99999
        for g in range(len(ground)):
            if max_g < ground[g]:
                max_g = ground[g]
                max_idx = g
        for g in range(len(ground)):
            if min_g > ground[g]:
                min_g = ground[g]
                min_idx = g
        if max_g-min_g<=1:
            print(f'#{t+1} {max_g-min_g}')
            break
    print(f'#{t + 1} {max_g - min_g}')

