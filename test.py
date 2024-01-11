test_case = int(input())

for test in range(test_case):
    N,M = map(int,input().split())
    Ai = list(map(int,input().split()))
    Bj = list(map(int,input().split()))
    sum_list = []
    times = 0
    while True:
        if N < M :
            for x in range(N):
                times += Ai[x]*Bj[x]
            sum_list.append(times)
            Ai.insert(0,0)
            N += 1
            times = 0
        elif N > M :
            for x in range(M):
                times += Ai[x]*Bj[x]
            sum_list.append(times)
            Bj.insert(0,0)
            M += 1
            times = 0
        else :
            for x in range(N):
                times += Ai[x]*Bj[x]
            sum_list.append(times)
            times = 0
            break  
    result = max(sum_list)
    print(f'#{test+1} {result}')    