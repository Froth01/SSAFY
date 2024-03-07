def prime_search(limit):
    primes = [True]*(limit+1)
    primes[0]=primes[1]=False
    for n in range(2,int(limit**0.5)+1):
        if primes[n]:
            for i in range(n*n,limit+1,n):
                primes[i] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]


M,N = map(int,input().split())
primes = prime_search(N)
for m in primes:
    if m>=M:
        print(m)