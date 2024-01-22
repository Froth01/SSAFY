N=int(input())
for n in range(1,N+1):
    print(' '*(N-n)+'*'*(-1+2*n))
for m in range(2*N-1,N,-1):
    print(' '*(abs(m-2*N))+'*'*(m+(m-2*N-1)))

    