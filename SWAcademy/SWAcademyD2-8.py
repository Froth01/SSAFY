#1945. 간단한 소인수분해
T=int(input())

for t in range(T):
    jisu=0
    N=int(input())
    while N!=1:
        list_jisu = [11,7,5,3,2]
        for j in list_jisu:
            if N%j==0:
                N//=j
                jisu += 10 ** list_jisu.index(j)
    test_case = '#'+str(t+1)
    print(test_case, *str(jisu).rjust(5,"0"))
