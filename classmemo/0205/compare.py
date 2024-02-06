T = int(input())
for t in range(T):
    N=input()
    M=input()
    result = 0
    for m in range(len(M)):
        if N[0]==M[m]:
            if N == M[m:m+len(N)] :
                result = 1
                break
    print(f'#{t+1} {result}')