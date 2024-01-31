T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    fly_list = []
    sum_kill = 0
    for n in range(N):
        fly_list.append(list(map(int,input().split())))
    for i in range(len(fly_list)):
        for j in range(len(fly_list)):
            smash = 0
            for mi in range(M):
                for mj in range(M):
                    if 0 <= i+mi <= N-1 and 0 <= j+mj <= N-1:
                        smash+=fly_list[i+mi][j+mj]
            if sum_kill < smash:
                sum_kill = smash
    print(f'#{t+1} {sum_kill}')