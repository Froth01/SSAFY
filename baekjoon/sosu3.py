def prime_search(limit):
    primes = [True]*(limit+1)
    primes[0]=primes[1]=False
    for n in range(2,int(limit**0.5)+1):
        if primes[n]:
            for i in range(n*n,limit+1,n):
                primes[i] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]


N = int(input())
primes = prime_search(N)
cnt = 0
for p in range(len(primes)):
    ing = 0
    for q in range(p,len(primes)):
        ing+=primes[q]
        if ing==N:
            cnt+=1
            break
        elif ing>N:
            break
print(cnt)