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
    
    for line in range(total_line):
        
        if len(Ci[line]*int(Ki[line]))<rest:
            rest=abs(rest-len(Ci[line]*int(Ki[line])))
            print(Ci[line]*int(Ki[line]),end='')
        elif len(Ci[line]*int(Ki[line]))==10:
            print(Ci[line]*int(Ki[line]))
        else:
            rest=abs(rest-len(Ci[line]*(int(Ki[line])-10)))
            print(Ci[line]*10)
            print(Ci[line]*(int(Ki[line])-10),end='')
            
            
            