T = int(input())
for t in range(T):
    str1 = input()
    str2 = input()
    N,M = len(str1), len(str2)
    for s in range(M-N+1):
        found = 1
        for i in range(N):
            if str1[i]!=str2[s+i]:
                found = 0
                break
        if found:
            print(f'#{t+1} {found}')
            break
    if found == 0:
        print(f'#{t+1} {found}')