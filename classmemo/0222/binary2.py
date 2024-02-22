T = int(input())
for t in range(T):
    N = float(input())
    result=''
    for n in range(1,13):
        if N==0:
            break
        elif N >= 2**(-n):
            N -= 2**(-n)
            result += '1'
        else:
            result += '0'
    if N!=0:
        result = 'overflow'
    print(f'#{t+1} {result}')

