T = int(input())
for t in range(T):
    N = input()
    M = input()
    max_str = 0
    for n in range(len(N)):
        cnt=0
        for m in range(len(M)):
            if N[n]==M[m]:
                cnt+=1
        if max_str<cnt:
            max_str=cnt
    print(f'#{t+1} {max_str}')