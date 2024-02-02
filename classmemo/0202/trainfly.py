def go_go(distance,A_speed,B_speed,F_speed,fly_di=0):
    gap_run = distance / (B_speed + F_speed)
    fly_di += (F_speed * gap_run)
    new_gap = (F_speed * gap_run) - (A_speed * gap_run)
    if new_gap<=10**(-7):
        return fly_di
    else:
        return go_go(new_gap,B_speed,A_speed,F_speed,fly_di)


T = int(input())
for t in range(T):
    D,A,B,F = map(int,input().split())
    print(f'#{t+1} {go_go(D,A,B,F)}')



