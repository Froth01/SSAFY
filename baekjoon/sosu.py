N,K = map(int,input().split())
cnt = 0
num = [n for n in range(2,N+1)]
while len(num)>=1:
    P=num[0]
    num.remove(P)
    cnt+=1
    if cnt == K:
        print(P)
        break
    for m in num:
        if m%P == 0 :
            num.remove(m)
            cnt+=1
            if cnt == K:
                print(m)
                break
