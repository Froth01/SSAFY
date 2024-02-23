T = int(input())
for t in range(T):
    case = input()
    num = '0'
    cnt = 0
    for c in case:
        if c!=num:
            num=c
            cnt+=1
    print(f'#{t+1} {cnt}')