T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    pizza = list(map(int,input().split()))
    oven = [[0,0]]*N
    cnt = 0
    Done = 0
    while Done!=N-1:
        for tray in range(len(oven)):
            if oven[tray][0]=='Done':
                continue
            elif oven[tray][0]//2==0:
                if pizza:
                    cnt+=1
                    oven[tray]=[pizza.pop(0),cnt]
                else:
                    oven[tray][0]='Done'
                    Done+=1
                    if Done==N-1:
                        break
            else:
                oven[tray][0]//=2
    for tray in oven:
        if tray[0]!='Done':
            result = tray[1]
            break
    print(f'#{t+1} {result}')