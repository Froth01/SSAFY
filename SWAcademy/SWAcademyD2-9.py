#1946. 간단한 압축 풀기
T=int(input())
for t in range(T):
    Ci=[]
    Ki=[]
    N=int(input())
    for n in range(N):
        a,b = input().split()
        Ci.append(a)
        Ki.append(int(b))
    total_len = sum(Ki)
    total_line = 0
    rest = 10
    if total_len % 10 != 0:
        total_line = (total_len//10)+1
    else :
        total_line = total_len//10
    print(f'#{t+1}')
    for line in range(total_line):
        if len(Ci[line]*Ki[line])>rest:
            print(Ci[line]*rest)
            print(Ci[line]*(Ki[line]-rest))
            rest =10-(Ki[line]-rest)%10
        elif len(Ci[line]*Ki[line])==rest:
            print(Ci[line]*Ki[line])
        elif len(Ci[line]*Ki[line])<rest:
            rest-=len(Ci[line]*Ki[line])
            print(Ci[line]*Ki[line],end='')
    print('\n')    
            