def baby_gin(lst):
    first_get = True
    result = 0
    for c in lst:
        if first_get:
            first_get=False
            P1[c]+=1
            for n in range(len(P1)):
                if P1[n]>=3:
                    result = 1
                    return result
                elif P1[n]>=1 and n<=len(P1)-3:
                    if P1[n+1]>=1 and P1[n+2]>=1:
                        result = 1
                        return result
        else:
            first_get=True
            P2[c] += 1
            for n in range(len(P2)):
                if P2[n] >= 3:
                    result = 2
                    return result
                elif P2[n]>=1 and n<=len(P2)-3:
                    if P2[n+1]>=1 and P2[n+2]>=1:
                        result = 2
                        return result
    return result
T = int(input())
for t in range(T):
    card = list(map(int,input().split()))
    P1 = [0]*10
    P2 = [0]*10
    print(f'#{t+1} {baby_gin(card)}')