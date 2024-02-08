def fac(num):
    nf = num
    if num == 0:
        return 1
    for n in range(1,num):
        nf=nf*(num-n)
    return nf

N,K = map(int,input().split())
print(fac(N)//(fac(N-K)*fac(K)))