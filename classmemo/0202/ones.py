T = int(input())
for t in range(T):
    N = int(input())
    num = input()
    cnt = 0
    maximum = 0
    for n in num:
        if n=='1':
            cnt+=1
            if maximum<cnt:
                maximum=cnt
        else:
            cnt=0
    print(f'#{t+1} {maximum}')