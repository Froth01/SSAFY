def prime_search(limit):
    primes = [True]*(limit+1)
    primes[0]=primes[1]=False
    for n in range(2,int(limit**0.5)+1):
        if primes[n]:
            for i in range(n*n,limit+1,n):
                primes[i] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]

T = int(input())
N,K = map(int,input().split())
primes = prime_search(n)
ing = 0
cnt = 0
answer = []
gether = []
while len(gether)!=K:
    for p in primes[::-1]:
        for q in primes
        if ing+primes[p]==N:
           gether.append(primes[p])
           answer.append(gether)
           gether.clear()
           cnt+=1
        elif ing+primes[p]<N:
           gether.append(primes[p])
           ing+=primes[p]
